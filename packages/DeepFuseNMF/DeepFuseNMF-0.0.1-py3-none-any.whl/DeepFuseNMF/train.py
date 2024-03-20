from torch.utils.data import DataLoader
from torch import nn
from torch.optim import Adam
from torch.optim.lr_scheduler import StepLR
import torch
import torch.nn.functional as F
import numpy as np
import pandas as pd

import cv2
import math
import os

from scipy.spatial import KDTree
from sklearn.decomposition import NMF
from sklearn.linear_model import LinearRegression
import types

from .data import HE_Prediction_Dataset, HE_Dataset, spatial_obj
from .model import DeepFuseNMFUnet, GraphAutoEncoder
from .utils import create_pseudo_spots, query_kdtree_parallel, construct_adjacency_matrix


class DeepFuseNMF_Runner:
    """
    The `DeepFuseNMF_Runner` class is a runner for the DeepFuseNMF model.

    Args:
        sections (dict): Dictionary containing the spatial objects for the sections.
        rank (int): The rank of the NMF model.
        results_path (str): The path to save the results.
        seed (int, optional): The seed for random number generation. Defaults to 123.
        verbose (bool, optional): Whether to print the progress or not. Defaults to False.

    Methods:
        get_NMF_score: Perform NMF and normalize the results.
        get_GCN_score: Get the smoothed GCN score for each section.
        get_VD_score: Get the VD score for each section.
        pretrain: Pretrain the DeepFuseNMF model based on the image prediction.
        train: Train the DeepFuseNMF model based on the image prediction and spot expression reconstruction.
        finetune: Fine-tune the DeepFuseNMF model based on the image prediction and spot expression reconstruction.
        get_DeepFuseNMF_score: Get the pixel-wised DeepFuseNMF score for each section.

        _tissus_separation: Divide the tissue area into sub-tissue regions based on split size and redundancy ratio.
        _crate_pseudo_spots: Create pseudo spots for the tissue sections.
        _get_nearby_spots: Get the nearby spots based on the feasible domain, radius, and real spot coordinates.
        _find_nearby_spots: Find the nearby spots based on the spot coordinates and the feasible domain.
        _calculate_splits: Calculate the splits for either rows or columns.
        _get_image_embedding: Get the image embeddings based on the spot coordinates, radius, and image.
        _train_GCN: Train the GCN model to predict spots' GCN score (including pseudo spots).
        _prepare_pretrain: Prepare the pre-training process for the DeepFuseNMF model.
        _pretrain_model: Pre-train the DeepFuseNMF model based on the image prediction.
        _prepare_GCN: Prepare the training process for the GCN model.

    Example:
        >>> sections = {}
        >>> rank = 10
        >>> results_path = 'results'
        >>> seed = 123
        >>> verbose = False
        >>> runner = DeepFuseNMF_Runner(sections=sections, rank=rank, results_path=results_path, seed=seed, verbose=verbose)
        >>> runner.get_NMF_score()
    """

    def __init__(self,
                 sections: dict,
                 rank: int,
                 results_path: str,
                 seed: int = 123,
                 verbose: bool = False):

        self.sections = sections
        self.num_genes = self.sections[list(self.sections.keys())[0]].spot_exp.shape[1]

        self.rank = rank
        self.results_path = results_path

        self.seed = seed
        self.verbose = verbose

        args_dict = {'num_channels': 3, 'split_size': 256, 'smooth_threshold': 0.01,
                     'redundant_ratio': 0.15, 'overlap_ratio': 0.2, 'bound_ratio': 0.05,

                     'num_workers': 4, 'batch_size': 32, 'lr': 0.003, 'weight_decay': 1e-5, 'lda': 0.05,
                     'step_size_pretrain': 5, 'gamma_pretrain': 0.5, 'n_epoch_pretrain': 100, 'n_epoch_pre_backbone': 20,
                     'step_size_GCN': 500, 'gamma_GCN': 0.8, 'n_epoch_GCN': 2000, 'rec_iter_GCN': 500,
                     'step_size_train': 10, 'gamma_train': 0.8, 'n_epoch_train': 50, 'rec_iter': 5,
                     'step_size_finetune': 5, 'gamma_finetune': 0.8, 'n_epoch_finetune': 25, 'rec_iter_finetune': 5}

        self.args = types.SimpleNamespace(**args_dict)
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        print(f'*** Using {self.device}... ***')

        self.GCN = None
        self.metagene = None

        self.model = DeepFuseNMFUnet(rank=self.rank, num_genes=self.num_genes, num_channels=self.args.num_channels)
        self.model.to(self.device)

        self.train_loader = None

        # Get the tissue splits and create pseudo spots
        if self.verbose: print('*** Preparing the tissue splits and creating pseudo spots... ***')
        self._tissus_separation()
        self._crate_pseudo_spots()

    def _crate_pseudo_spots(self):
        # Create pseudo spots for the tissue sections.

        for _, section in self.sections.items():
            # Get the section details
            feasible_domain = section.feasible_domain
            radius = section.radius
            real_spot_coord = section.spot_coord

            # Get the image embeddings
            pseudo_spot_coord = create_pseudo_spots(feasible_domain=feasible_domain, radius=radius, seed=self.seed)
            section.all_spot_coord = np.vstack((real_spot_coord, pseudo_spot_coord))

        # Get the nearby spots based on different settings
        self._get_nearby_spots(use_all_spot=False, use_section_range=False)
        self._get_nearby_spots(use_all_spot=True, use_section_range=False)
        self._get_nearby_spots(use_all_spot=True, use_section_range=True)

    def get_NMF_score(self):
        # Perform NMF and normalize the results.

        # Prepare data
        spot_exp = np.vstack([self.sections[section].spot_exp for section in self.sections])

        # Perform NMF
        print('*** Performing NMF... ***')

        model_NMF = NMF(n_components=self.rank, init='nndsvd', random_state=self.seed, max_iter=2000)
        NMF_score = model_NMF.fit_transform(spot_exp)
        metagene = model_NMF.components_

        # Normalize the results of NMF
        region_NMF_max = np.max(NMF_score, axis=0)
        NMF_score_normalized = NMF_score / region_NMF_max
        metagene_normalized = pd.DataFrame(metagene * region_NMF_max[:, np.newaxis])

        # Save the results
        metagene_normalized.to_csv(f'{self.results_path}/V_para_NMF.csv')

        start_i = 0
        for _, section in self.sections.items():
            end_i = start_i + section.num_spots
            section.scores['NMF'] = NMF_score_normalized[start_i:end_i]
            start_i = end_i


    def _get_nearby_spots(self,
                          use_all_spot: bool = False,
                          use_section_range: bool = False):
        """
        Get the nearby spots based on the feasible domain, radius, and real spot coordinates.

        Args:
            use_all_spot (bool): Whether to use all spots or not.
            use_section_range (bool): Whether to use the section range or not.
        """

        for _, section in self.sections.items():
            # Get the section details
            feasible_domain = section.feasible_domain
            spot_coord = section.all_spot_coord if use_all_spot else section.spot_coord

            # Find the nearest spots
            if use_section_range:
                row_range, col_range = section.row_range, section.col_range
            else:
                row_range, col_range = feasible_domain.shape

            nearby_spots = self._find_nearby_spots(spot_coord=spot_coord, row_range=row_range, col_range=col_range)

            if use_section_range:
                section.vd_nearby_spots = nearby_spots
            else:
                if use_all_spot:
                    section.all_nearby_spots = nearby_spots
                else:
                    section.nearby_spots = nearby_spots

    def _find_nearby_spots(self,
                           spot_coord: np.ndarray,
                           row_range: tuple | int,
                           col_range: tuple | int) -> np.ndarray:
        """
        Find the nearby spots based on the spot coordinates and the feasible domain.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            row_range (tuple | int): Tuple indicating the start and end row for the feasible domain.
            col_range (tuple | int): Tuple indicating the start and end column for the feasible domain.

        Returns:
            numpy.ndarray: Array of nearby spots.
        """

        # KDTree for nearest spot querying
        tree = KDTree(spot_coord)

        # Create grid for querying nearest spots
        if row_range.__class__ is not tuple:
            query_grid = np.vstack(
                (np.repeat(np.arange(row_range), col_range), np.tile(np.arange(col_range), row_range))).T
        else:
            query_grid = np.vstack((np.repeat(np.arange(row_range[0], row_range[1]), col_range[1] - col_range[0]),
                                    np.tile(np.arange(col_range[0], col_range[1]), row_range[1] - row_range[0]))).T

        return query_kdtree_parallel(tree, query_grid, workers=4)

    # Get the tissue splits
    def _tissus_separation(self):
        # Divide the tissue area into sub-tissue regions based on split size and redundancy ratio.

        for name, section in self.sections.items():
            image = section.image
            section.tissue_coord = {}

            # Obtain min and max values for row and column
            row_min, row_max = 0, image.shape[1]
            col_min, col_max = 0, image.shape[2]

            # Calculate row and column splits
            row_splits = self._calculate_splits(row_min, row_max)
            col_splits = self._calculate_splits(col_min, col_max)

            # Combine row and column splits to form sub-tissue coordinates
            sub_tissue_coord = np.vstack((np.repeat(row_splits[:, 0], len(col_splits)),
                                          np.repeat(row_splits[:, 1], len(col_splits)),
                                          np.tile(col_splits[:, 0], len(row_splits)),
                                          np.tile(col_splits[:, 1], len(row_splits)))).T

            section.tissue_coord['whole'] = sub_tissue_coord

            # ---------------------------------------------- #

            # Obtain min and max values for row and column
            row_min, row_max = section.row_range
            col_min, col_max = section.col_range

            # Calculate row and column splits
            row_splits = self._calculate_splits(row_min, row_max)
            col_splits = self._calculate_splits(col_min, col_max)

            # Combine row and column splits to form sub-tissue coordinates
            sub_tissue_coord = np.vstack((np.repeat(row_splits[:, 0], len(col_splits)),
                                          np.repeat(row_splits[:, 1], len(col_splits)),
                                          np.tile(col_splits[:, 0], len(row_splits)),
                                          np.tile(col_splits[:, 1], len(row_splits)))).T

            section.tissue_coord['VD'] = sub_tissue_coord

    def _calculate_splits(self,
                          min_val: int,
                          max_val: int) -> np.ndarray:
        """
        Calculate the splits for either rows or columns.

        Args:
            min_val (int): The minimum value for the split.
            max_val (int): The maximum value for the split.

        Returns:
            numpy.ndarray: Array of split indices.
        """

        redundant_size = round(self.args.split_size * self.args.redundant_ratio)
        num_splits = int(np.ceil((max_val - min_val - redundant_size) / (self.args.split_size - redundant_size)))

        start_indices = np.arange(min_val, min_val + num_splits * (self.args.split_size - redundant_size),
                                  self.args.split_size - redundant_size)
        end_indices = start_indices + self.args.split_size
        if end_indices[-1] > max_val:
            end_indices[-1] = max_val
            start_indices[-1] = max_val - self.args.split_size

        return np.vstack((start_indices, end_indices)).T

    def pretrain(self, pretrain_path):
        """
        Pre-train the DeepFuseNMF model based on the image prediction.

        Args:
            pretrain_path (str): The path to save the pre-trained model.
        """

        # Pretraining mode: only train the backbone based on the image prediction
        self.model.training_mode = False

        if os.path.exists(pretrain_path):
            print(f'*** Load pre-trained model from {pretrain_path} ***')
            self.model.load_state_dict(torch.load(pretrain_path))
        else:
            self._pretrain_model()
            print(f'*** Save pre-trained model to {pretrain_path} ***')
            torch.save(self.model.state_dict(), pretrain_path)

    def _prepare_pretrain(self):
        # Prepare the pre-training process for the DeepFuseNMF model.

        self.model.train()

        # Prepare the training dataset
        self.train_dataset = torch.utils.data.ConcatDataset([
            HE_Prediction_Dataset(section=section, args=self.args) for name, section in self.sections.items()
        ])

        # Prepare the training loader
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.args.batch_size, shuffle=True,
                                       drop_last=False, num_workers=self.args.num_workers)

        # Prepare the loss, optimizer and scheduler
        self.loss = nn.MSELoss()
        self.optimizer = Adam(self.model.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay)
        self.scheduler = StepLR(self.optimizer, step_size=self.args.step_size_pretrain, gamma=self.args.gamma_pretrain)

    def _pretrain_model(self):
        # Prepare the pre-training process
        self._prepare_pretrain()

        # Fix the backbone
        for name, p in self.model.named_parameters():
            p.requires_grad = False if name.split(".")[0] == "backbone" else True

        # Start the pre-training process
        last_loss = 1000.
        epoch_loss = 0.
        for epoch in range(self.args.n_epoch_pretrain):

            if epoch >= self.args.n_epoch_pre_backbone:
                for name, p in self.model.named_parameters():
                    p.requires_grad = True

            for i, img in enumerate(self.train_loader):
                img = img.to(self.device)
                out, _ = self.model(img)

                loss = self.loss(out, img)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                if self.verbose: epoch_loss += loss.item()

            # Early stopping if the loss does not change much
            if self.args.n_epoch_pretrain==50 and abs(last_loss - epoch_loss) / epoch_loss < 0.01:
                print("Reached convergence, stopping early")
                break

            if self.verbose and (epoch + 1) % self.args.rec_iter == 0:
                print(f'Epoch: {epoch + 1}, Loss:{epoch_loss / (i + 1):.6f}')

            last_loss = epoch_loss
            epoch_loss = 0.
            self.scheduler.step()

    def _get_image_embedding(self,
                             spot_coord: np.ndarray,
                             radius: int,
                             image: np.ndarray,
                             batch_size: int = 32,
                             embedding_size: int = 256) -> np.ndarray:
        """
        Get the image embeddings based on the spot coordinates, radius, and image.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            radius (int): The radius within which to find coordinates.
            image (numpy.ndarray): sub-image.
            batch_size (int): The batch size for the image embeddings.
            embedding_size (int): The size of the image embeddings.

        Returns:
            numpy.ndarray: Array of image embeddings.
        """

        self.model.eval()

        # Extract sub-images and upsample to 256x256
        sub_images = nn.UpsamplingBilinear2d(size=256)(self._extract_image(spot_coord, radius, image))

        # Extract image embeddings
        image_embeddings = np.zeros((sub_images.shape[0], embedding_size))
        with torch.no_grad():
            for start_i in range(0, sub_images.shape[0], batch_size):
                end_i = min(start_i + batch_size, sub_images.shape[0])
                _, embeddings_batch = self.model(sub_images[start_i:end_i].to(self.device))
                image_embeddings[start_i:end_i] = torch.mean(embeddings_batch, dim=(2, 3)).cpu().numpy()

        return image_embeddings

    def _extract_image(self,
                       spot_coord: np.ndarray,
                       radius: int,
                       image: np.ndarray) -> torch.Tensor:
        """
        Extract the sub-image based on the spot coordinates, radius, and image.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            radius (int): The radius within which to find coordinates.
            image (numpy.ndarray): Original image.

        Returns:
            torch.Tensor: The sub-image tensor.
        """

        img_size = radius * 2
        num_spots = spot_coord.shape[0]
        sub_images = np.zeros((num_spots, 3, 2 * img_size + 1, 2 * img_size + 1), dtype=np.float32)

        # Extract sub-image for each spot
        for spot_index in range(num_spots):
            center_row, center_col = round(spot_coord[spot_index, 0]), round(spot_coord[spot_index, 1])
            row_start, row_end = max(0, center_row - img_size + 1), min(image.shape[1] - 1, center_row + img_size + 1)
            col_start, col_end = max(0, center_col - img_size + 1), min(image.shape[2] - 1, center_col + img_size + 1)

            if row_start == 0: row_end = 2 * img_size
            if col_start == 0: col_end = 2 * img_size
            if row_end == image.shape[1] - 1: row_start = image.shape[1] - 1 - 2 * img_size
            if col_end == image.shape[2] - 1: col_start = image.shape[2] - 1 - 2 * img_size

            sub_images[spot_index, :, :, :] = image[:, row_start:row_end + 1, :][:, :, col_start:col_end + 1]

        return torch.tensor(sub_images)

    def _prepare_GCN(self,
                     adj_matrix: np.ndarray,
                     num_spots: int):
        """
        Prepare the training process for the GCN model.

        Args:
            adj_matrix (numpy.ndarray): The adjacency matrix of the graph.
            num_spots (int): The number of spots in the dataset.
        """

        # Prepare the GCN model
        adj_matrix = torch.tensor(adj_matrix, dtype=torch.float32, device=self.device, requires_grad=False)
        self.GCN = GraphAutoEncoder(adj_matrix=adj_matrix, num_spots=num_spots, rank=self.rank).to(self.device)
        self.GCN.train()

        # Prepare the loss, optimizer and scheduler
        self.loss = nn.MSELoss()
        self.optimizer = Adam(self.GCN.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay)
        self.scheduler = StepLR(self.optimizer, step_size=self.args.step_size_GCN, gamma=self.args.gamma_GCN)

        # step 500, gamma 0.8
        # n_epoch_GCN 2000

    def _train_GCN(self,
                  adj_matrix: np.ndarray,
                  score: np.ndarray) -> np.ndarray:
        """
        Train the GCN model to predict spots' GCN score (including pseudo spots).

        Args:
            adj_matrix (numpy.ndarray): The adjacency matrix of the graph.
            score (numpy.ndarray): Array of spot scores.

        Returns:
            numpy.ndarray: Array of predicted spot scores.
        """

        score = torch.tensor(np.array(score), dtype=torch.float32, device=self.device)
        num_spots = score.shape[0]
        self._prepare_GCN(adj_matrix, num_spots)

        # Train the GCN model
        loss_cur = 0.
        for epoch in range(self.args.n_epoch_GCN):
            self.optimizer.zero_grad()

            pred = self.GCN(score)[:num_spots, :]
            loss = self.loss(pred, score)
            loss.backward()
            self.optimizer.step()
            self.scheduler.step()

            if self.verbose:
                loss_cur = loss_cur + loss.item()
                if (epoch + 1) % self.args.rec_iter_GCN == 0:
                    print(f'Epoch: {epoch+1}, Average Loss:{loss_cur / self.args.rec_iter_GCN:.20f}')
                    loss_cur = 0.

        # Get the predicted spot scores
        self.GCN.eval()
        with torch.no_grad():
            return self.GCN(score).cpu().detach().numpy()

    def get_GCN_score(self):
        # Get the smoothed GCN score for each section.

        print('*** Performing GCN... ***')

        for _, section in self.sections.items():
            # Get the section details
            radius = section.radius
            image = section.image
            NMF_score = section.scores['NMF']

            # Get the image embeddings
            all_image_embeddings = self._get_image_embedding(section.all_spot_coord, radius, image)

            # Construct the adjacency matrix
            adjacency_matrix = construct_adjacency_matrix(spot_coord=section.all_spot_coord,
                                                          spot_embeddings=all_image_embeddings,
                                                          num_real_spots=NMF_score.shape[0])

            # Train the GCN
            if self.verbose: print(f'*** Training GCN for {section.section_name}... ***')
            section.scores['GCN'] = self._train_GCN(adjacency_matrix, NMF_score)

        # refine the metagene_init
        LR = LinearRegression(fit_intercept=False, positive=True)
        LR_result = LR.fit(
            np.vstack([section.scores['GCN'][:section.num_spots, :] for _, section in self.sections.items()]),
            np.vstack([section.spot_exp for _, section in self.sections.items()]))

        self.metagene = LR_result.coef_.T

    def _smooth(self,
                spot_score: np.ndarray,
                kernel_size: int,
                threshold: float = 0.01) -> np.ndarray:
        """
        Smooths the input spot score tensor using iterative blurring until the mean change between iterations is below a specified threshold or a maximum number of iterations is reached.

        Args:
            spot_score (numpy.ndarray): Array containing spot scores.
            kernel_size (int): The size of the kernel for blurring.
            threshold (float, optional): The threshold for mean change between iterations. Defaults to 0.01.

        Returns:
            spot_score (numpy.ndarray): smoothed spot scores.
        """

        for i in range(spot_score.shape[0]):
            smooth_input = spot_score[i, :, :]  # Input for the first iteration

            # Iterative blurring until mean change is less than threshold or max iterations reached
            for _ in range(10):
                smooth_output = cv2.blur(smooth_input, (kernel_size, kernel_size), cv2.BORDER_DEFAULT)
                diff_mat1 = (abs(smooth_input - smooth_output))
                nonzero_index = np.where(diff_mat1 != 0)
                mean_change = diff_mat1[nonzero_index[0], nonzero_index[1]].mean()

                smooth_input = smooth_output  # Update input for next iteration

                if mean_change < threshold: break

            spot_score[i, :, :] = smooth_output  # Update the region with smoothed values

        return spot_score

    def get_VD_score(self, use_score='GCN'):
        """
        Visualize domains for spatial transcriptomics data, optionally with spot-wise embedding.

        Args:
            use_score (str): The type of embedding to be visualized.
        """

        for name, section in self.sections.items():
            # Get the extended score
            extended_score = self._get_extended_score(section, use_score, use_all_pixel=False)

            # Get the coordinates for the tissue
            num_images = section.tissue_coord['VD'].shape[0]
            tmp_coords = section.tissue_coord['VD'].copy()
            tmp_coords[:, :2] -= section.row_range[0]
            tmp_coords[:, 2:] -= section.col_range[0]

            # Get the VD score for each patch
            VD_score = []
            for i in range(num_images):
                VD_score.append(extended_score[:, tmp_coords[i, 0]:tmp_coords[i, 1], tmp_coords[i, 2]:tmp_coords[i, 3]])

            section.scores['VD'] = np.array(VD_score)

    def _get_extended_score(self,
                            section: spatial_obj,
                            use_score: str = 'GCN',
                            use_all_pixel: bool = False) -> np.ndarray:
        """
        Get the extended score for the given section.

        Args:
            section (spatial_obj): The spatial object.
            use_score (str): The type of embedding to be visualized.
            use_all_pixel (bool, optional): Whether to use all pixels or not. Defaults to False.

        Returns:
            extended_score (numpy.ndarray): Array of extended scores.
        """

        # Determine the range and nearby spots
        if use_all_pixel:
            row_range, col_range = (0, section.feasible_domain.shape[0]), (0, section.feasible_domain.shape[1])
            nearby_spots = section.all_nearby_spots
        else:
            row_range, col_range = section.row_range, section.col_range
            nearby_spots = section.vd_nearby_spots

        # Get the spot score, kernel size, and feasible domain
        spot_score = section.scores[use_score]
        kernel_size = section.kernel_size
        feasible_domain = section.feasible_domain[row_range[0]:row_range[1], col_range[0]:col_range[1]]

        # Get the extended score
        extended_score = np.reshape(spot_score[nearby_spots, :],
                                    (row_range[1] - row_range[0], col_range[1] - col_range[0], -1))
        extended_score = np.transpose(extended_score, (2, 0, 1))
        extended_score = self._smooth(extended_score, kernel_size, threshold=self.args.smooth_threshold)
        extended_score = extended_score * np.expand_dims(feasible_domain, axis=0)

        return extended_score

    def _prepare_train(self,
                       load_decoder_params: bool = True):
        """
        Prepare the training process for the DeepFuseNMF model.

        Args:
            load_decoder_params: Whether to load the decoder parameters or not.
        """

        # Prepare the training dataset
        self.train_dataset = torch.utils.data.ConcatDataset(
            [HE_Dataset(section=section, args=self.args) for name, section in self.sections.items()]
        )

        # Prepare the training loader
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.args.batch_size, shuffle=True,
                                       drop_last=False, num_workers=0, collate_fn=lambda x: x)
        self.num_batches = len(self.train_loader)

        # Load the decoder parameters
        if load_decoder_params:
            self.model.nmf_decoder.data = torch.tensor(self.metagene.T, dtype=torch.float32, device=self.device,
                                                       requires_grad=True)

        # Set the model to training mode
        self.model.train()
        for name, p in self.model.named_parameters():
            p.requires_grad = True

        # Prepare the loss and optimizer
        self.loss_img = nn.MSELoss()
        self.loss_exp = nn.PoissonNLLLoss(log_input=False, reduction="mean")

        self.optimizer = Adam(self.model.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay)

    def train(self,
              train_path: str):
        """
        Train the DeepFuseNMF model based on the image prediction and spot expression reconstruction.

        Args:
            train_path: The path to save the trained model.
        """

        self.model.training_mode = True

        if os.path.exists(train_path):
            print(f'*** Load trained model from {train_path} ***')
            self.model.load_state_dict(torch.load(train_path))
        else:
            self._train_model()
            print(f'*** Save trained model to {train_path} ***')
            torch.save(self.model.state_dict(), train_path)

    def _train_model(self):
        # Train the DeepFuseNMF model

        self._prepare_train(load_decoder_params=True)
        self.scheduler = StepLR(self.optimizer, step_size=self.args.step_size_train, gamma=self.args.gamma_train)

        if self.verbose: print('*** Training the model... ***')

        loss_all_epoch, loss_image_epoch, loss_exp_epoch = [], [], []
        part_update = "P2"

        # Train the model
        for epoch in range(self.args.n_epoch_train):

            # weight determination
            if epoch < 10:
                weight_image, weight_exp = 0., 1.
                for name, p in self.model.named_parameters():
                    if name == "nmf_decoder": p.requires_grad = False

            elif epoch < 20:
                weight_image = weight_exp = 0.5
                for name, p in self.model.named_parameters():
                    p.requires_grad = True if name.split(".")[0] == "image_pred" else False

            else:
                loss_image_ratio = math.exp(loss_image_epoch[-1] / loss_image_epoch[-2])
                loss_exp_ratio = math.exp(loss_exp_epoch[-1] / loss_exp_epoch[-2])
                weight_image = loss_image_ratio / (loss_image_ratio + loss_exp_ratio)
                weight_exp = loss_exp_ratio / (loss_image_ratio + loss_exp_ratio)

                if epoch % 5 == 0:
                    part_update = "P2" if part_update == "P1" else "P1"
                    if self.verbose: print(f'Epoch: {epoch + 1}, turn to {part_update} update')

                # For part1, fix the update of the image_pred and nmf_decoder
                if part_update == "P1":
                    for name, p in self.model.named_parameters():
                        p.requires_grad = False if name == "nmf_decoder" or name.split(".")[0] == "image_pred" else True

                # For part2, only update the image_pred and nmf_decoder
                if part_update == "P2":
                    for name, p in self.model.named_parameters():
                        p.requires_grad = True if name == "nmf_decoder" or name.split(".")[0] == "image_pred" else False

            if (epoch+1) % self.args.rec_iter == 0 and self.verbose:
                print(f'Epoch: {epoch + 1}, weight_image:{weight_image:.5f}, weight_exp:{weight_exp:.5f}')

            loss_all_tmp, loss_image_tmp, loss_exp_tmp = 0., 0., 0.

            for data in self.train_loader:
                loss = 0.

                for sub_img, spot_exp, feasible_coord, vd_score in data:
                    sub_img = torch.tensor(sub_img, dtype=torch.float32, device=self.device).unsqueeze(0)
                    vd_score = torch.tensor(vd_score, dtype=torch.float32, device=self.device).unsqueeze(0)
                    spot_exp = torch.tensor(spot_exp, dtype=torch.float32, device=self.device) if len(feasible_coord) > 0 else None

                    image_pred, spot_exp_pred, HR_score = self.model(sub_img, feasible_coord, vd_score)

                    # Calculate the loss
                    loss_image = self.loss_img(image_pred, sub_img) / len(data)
                    loss_exp = self.loss_exp(spot_exp_pred, spot_exp) / len(data) if spot_exp is not None else 0.

                    if weight_image == 0.:
                        loss = loss + weight_exp * loss_exp
                    elif weight_exp == 0.:
                        loss = loss + weight_image * loss_image
                    else:
                        loss = loss + weight_image * loss_image + weight_exp * loss_exp

                    # Regularization term
                    idx = torch.where(vd_score.sum([0, 2, 3]) < 0.1)[0]
                    if len(idx) > 0:
                        loss = loss + self.args.lda * F.mse_loss(HR_score[0, idx, :, :], vd_score[0, idx, :, :]) / len(data)

                    loss_image_tmp += loss_image.item()
                    loss_exp_tmp += loss_exp.item() if spot_exp is not None else 0.

                loss_all_tmp += loss.item()

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            # Record the losses
            loss_all_epoch.append(loss_all_tmp / self.num_batches)
            loss_image_epoch.append(loss_image_tmp / self.num_batches)
            loss_exp_epoch.append(loss_exp_tmp / self.num_batches)

            if self.verbose and (epoch+1) % self.args.rec_iter == 0:
                print(f'Epoch: {epoch + 1}, AllLoss:{loss_all_epoch[-1]:.5f}, ImageLoss:{loss_image_epoch[-1]:.5f}, ExpLoss:{loss_exp_epoch[-1]:.5f}')

            self.scheduler.step()

    def finetune(self,
                 finetune_path: str):
        """
        Finetune the DeepFuseNMF model based on the image prediction and spot expression reconstruction.

        Args:
            finetune_path (str): The path to save the finetuned model.
        """

        self.model.training_mode = True
        if self.train_loader is None:
            self._prepare_train(load_decoder_params=False)
        else:
            for param_group in self.optimizer.param_groups:
                param_group['lr'] = self.args.lr
            self.scheduler = StepLR(self.optimizer, step_size=self.args.step_size_finetune, gamma=self.args.gamma_finetune)

        if os.path.exists(finetune_path):
            print(f'*** Load finetune model from {finetune_path} ***')
            self.model.load_state_dict(torch.load(finetune_path))
        else:
            self._finetune_model()
            print(f'*** Save fine-tuned model to {finetune_path} ***')
            torch.save(self.model.state_dict(), finetune_path)

        # Save the NMF decoder parameters
        np.savetxt(f'{self.results_path}/V_para_final.csv',
                   np.array(self.model.nmf_decoder.data.cpu().detach().numpy().T), delimiter=",")

    def _finetune_model(self):
        if not self.model.training_mode: self._prepare_train()

        if self.verbose: print('*** Finetuning the model... ***')

        # only train the low_rank module when the epoch is smaller than 10
        for name, p in self.model.named_parameters():
            p.requires_grad = True if name in ("low_rank.9.weight", "low_rank.9.bias", "low_rank.10.weight", "low_rank.10.bias") else False

        for epoch in range(self.args.n_epoch_finetune):
            # Only train the low_rank module when the epoch is smaller than 10

            if epoch >= 10:
                for name, p in self.model.named_parameters():
                    p.requires_grad = True if name == "nmf_decoder" else False

            if epoch >= 20:
                for name, p in self.model.named_parameters():
                    p.requires_grad = True if name in ("low_rank.9.weight", "low_rank.9.bias", "low_rank.10.weight", "low_rank.10.bias") else False

            loss_all_tmp, loss_image_tmp, loss_exp_tmp = 0., 0., 0.

            # Train the model
            for data in self.train_loader:
                loss = 0.

                for sub_img, spot_exp, feasible_coord, vd_score in data:
                    if len(feasible_coord) == 0 and epoch >= 10: continue

                    sub_img = torch.tensor(sub_img, dtype=torch.float32, device=self.device).unsqueeze(0)
                    vd_score = torch.tensor(vd_score, dtype=torch.float32, device=self.device).unsqueeze(0)
                    spot_exp = torch.tensor(spot_exp, dtype=torch.float32, device=self.device) if len(feasible_coord) > 0 else None

                    if epoch < 10:
                        # Only train the low_rank module based on the image prediction
                        image_pred, spot_exp_pred, HR_score = self.model(sub_img, {}, vd_score)
                        loss = loss + self.loss_img(image_pred, sub_img) / len(data)
                    else:
                        # Only train the nmf_decoder module based on the spot expression reconstruction
                        image_pred, spot_exp_pred, HR_score = self.model(sub_img, feasible_coord, vd_score)
                        loss = loss + self.loss_exp(spot_exp_pred, spot_exp) / len(data)

                    # Regularization term
                    idx = torch.where(vd_score.sum([0, 2, 3]) < 0.01)[0]
                    if len(idx) > 0:
                        loss = loss + self.args.lda * F.mse_loss(HR_score[0, idx, :, :], vd_score[0, idx, :, :]) / len(data)

                loss_all_tmp += loss.item()

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            if (epoch + 1) % self.args.rec_iter_finetune == 0:
                print(f'Epoch: {epoch + 1}, Loss:{loss_all_tmp / self.num_batches:.5f}')

            self.scheduler.step()

    def get_DeepFuseNMF_score(self,
                              suffix: str = None):
        """
        Extract the DeepFuseNMF scores for each section.

        Args:
            suffix (str): The suffix for the extracted scores.
        """

        self.model.eval()

        for name, section in self.sections.items():
            if self.verbose: print(f'*** Extracting DeepFuseNMF scores for {name}... ***')

            image = section.image

            # Get the extended score
            extended_score = self._get_extended_score(section, use_all_pixel=True)

            # Get the DeepFuseNMF scores
            if suffix is None:
                score_name = 'DeepFuseNMF'
            else:
                score_name = f'DeepFuseNMF_{suffix}'
                section.save_paths[score_name] = f"{section.save_paths['DeepFuseNMF']}_{suffix}"

            section.scores[score_name] = self._extract_embedding(image, extended_score)

    def _extract_embedding(self,
                           image: np.ndarray,
                           extended_score: np.ndarray) -> np.ndarray:
        """
        Extract the embedding based on the image and extended score.

        Args:
            image (numpy.ndarray): The image.
            extended_score (numpy.ndarray): The extended score.

        Returns:
            numpy.ndarray: The extracted embedding.
        """

        # Calculate the settings (e.g., bound width, overlap, etc.)
        bound_width = math.ceil(self.args.bound_ratio * self.args.split_size)
        overlap = math.floor(self.args.overlap_ratio * self.args.split_size)
        num_row, num_col = math.ceil(image.shape[1] / (self.args.split_size - overlap + 1)), math.ceil(
            image.shape[2] / (self.args.split_size - overlap + 1))

        # Frame is used to avoid the boundary effect
        frame = np.zeros((self.args.split_size, self.args.split_size))
        frame[bound_width:-bound_width, bound_width:-bound_width] = 1

        counts = np.zeros((image.shape[1], image.shape[2]), dtype=np.float32)
        embeddings = np.zeros((self.rank, image.shape[1], image.shape[2]), dtype=np.float32)

        # Extract the embedding
        for i in range(num_row):
            row_start = i * (self.args.split_size - overlap)
            if i == num_row - 1 and image.shape[1] - row_start < self.args.split_size: row_start = image.shape[1] - self.args.split_size

            for j in range(num_col):
                col_start = j * (self.args.split_size - overlap)
                if j == num_col - 1 and image.shape[2] - col_start < self.args.split_size: col_start = image.shape[2] - self.args.split_size

                # Extract the sub-image and sub-score
                sub_image = image[:, row_start:row_start + self.args.split_size, col_start:col_start + self.args.split_size]
                sub_score = extended_score[:, row_start:row_start + self.args.split_size, col_start:col_start + self.args.split_size]
                sub_image = torch.tensor(sub_image, dtype=torch.float32, device=self.device).unsqueeze(0)
                sub_score = torch.tensor(sub_score, dtype=torch.float32, device=self.device).unsqueeze(0)

                # Extract the embedding for the sub-image
                with torch.no_grad():
                    sub_embedding = self.model(image=sub_image, vd_score=sub_score, encode_only=True)
                sub_embedding = sub_embedding.squeeze().cpu().numpy()

                # Update the embeddings and counts
                embeddings[:, row_start: row_start + self.args.split_size, col_start: col_start + self.args.split_size] += sub_embedding * frame[np.newaxis, :, :]
                counts[row_start: row_start + self.args.split_size, col_start: col_start + self.args.split_size] += frame

        counts[counts == 0] = 1.

        # Return the average embeddings
        return embeddings / np.expand_dims(counts, axis=0)


