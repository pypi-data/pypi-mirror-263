import numpy as np
import os
import cv2
import math
import random
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

from ..data import spatial_obj 

def visualize_score(section: spatial_obj,
                    use_score: str,
                    index: int = None,
                    spot_wise: bool = False,
                    GMM_filter: bool = False):
    """
    Visualize the embeddings of the given section.

    Args:
        section (spatial_obj): The spatial object containing the section.
        use_score (str): The type of embedding to be visualized.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
        spot_wise (bool, optional): Whether to visualize spot-wise embeddings. Defaults to False.
        GMM_filter (bool, optional): Whether to use Gaussian Mixture Model for filtering low signal. Defaults to False.
    """

    rank = section.scores[use_score].shape[1]
    if index is None: index = random.randint(0, rank - 1)
    assert 0 <= index < rank, "The index is out of range."

    save_score(sections={section.section_name: section},
               use_score=use_score,
               index=index,
               spot_wise=spot_wise,
               GMM_filter=GMM_filter)
    
def save_score(sections: dict,
               use_score: str,
               index: int = None,
               spot_wise: bool = False,
               GMM_filter: bool = False,
               verbose: bool = False):
    """
    save score for given spot coordinates and region scores.

    Args:
        sections (dict): Dictionary containing the sections.
        use_score (str): The type of embedding to be visualized.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
        spot_wise (bool, optional): Whether to visualize spot-wise embeddings. Defaults to False.
        GMM_filter (bool, optional): Whether to use Gaussian Mixture Model for filtering low signal. Defaults to False.
        verbose (bool, optional): Whether to enable verbose output. Defaults to False.
    """

    if verbose: print(f"*** Saving the embeddings of {use_score}... ***")

    # Visualize the embeddings of each section
    for _, section in sections.items():
        # Get section attributes
        feasible_domain = section.feasible_domain
        radius = section.radius
        spot_score = section.scores[use_score]
        save_path = section.save_paths[use_score]

        if index is None:
            os.makedirs(save_path, exist_ok=True)
            np.save(f'{save_path}/{use_score}_score.npy', spot_score)

        # Visualize DeepFuseNMF embeddings
        if 'DeepFuseNMF' in use_score:
            visualize_deepfusenmf(all_score=spot_score, save_path=save_path + '/abs_cut/', index=index,
                                  feasible_domain=feasible_domain, cutoff_type="absolute_value")
            visualize_deepfusenmf(all_score=spot_score, save_path=save_path + '/quantile_cut/', index=index,
                                  feasible_domain=feasible_domain, cutoff_type="quantile")
            continue

        # Get spot coordinates and nearby spots
        if use_score == 'NMF':
            spot_coord, nearby_spots = section.spot_coord, section.nearby_spots
        else:
            spot_coord, nearby_spots = section.all_spot_coord, section.all_nearby_spots

        # Filter low signal using Gaussian Mixture Model
        if GMM_filter:
            for idx in range(spot_score.shape[1]):
                if index is not None and index != idx: continue
                
                data_use = spot_score[:, idx].reshape(spot_score.shape[0], 1)
                gmm = GaussianMixture(2, covariance_type='full', random_state=0).fit(data_use)
                label_choose = np.argmax(gmm.means_)
                labels = gmm.predict(data_use)
                signal_remove_index = np.where(labels != label_choose)[0]
                spot_score[signal_remove_index, idx] = 0

        # Perform visualization
        visualize_domains(nearby_spots=nearby_spots, spot_score=spot_score, index=index,
                          save_path=save_path, feasible_domain=feasible_domain)

        # Visualize spot-wise embeddings
        if spot_wise:
            visualize_domains_spot_wise(spot_coord=spot_coord, spot_score=spot_score, index=index,
                                        save_path=save_path + '/spot_wise/',
                                        feasible_domain=feasible_domain, radius=radius)

def visualize_domains(nearby_spots: np.ndarray,
                      spot_score: np.ndarray,
                      save_path: str,
                      feasible_domain: np.ndarray,
                      index: int = None):
    """
    Visualize domains for spatial transcriptomics data.

    Args:
        nearby_spots (numpy.ndarray): Array containing nearby spots.
        spot_score (numpy.ndarray): Array containing spot scores or region profiles.
        save_path (str): Path where the visualizations will be saved.
        feasible_domain (numpy.ndarray): Array indicating feasible domains for masking the visualization.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
    """

    # Get extended score and reshape
    row_range, col_range = feasible_domain.shape
    extended_score = spot_score[nearby_spots, :]
    reshaped_score = np.reshape(extended_score, (row_range, col_range, spot_score.shape[1]))

    # Visualize embedding for each dimension
    for idx in range(spot_score.shape[1]):
        if index is not None: idx = index
        
        tmp_score = reshaped_score[:, :, idx]
        normalized_score = tmp_score / tmp_score.max() * 255
        filtered_score = normalized_score * feasible_domain
        
        # Visualize score of the specific index
        if index is not None:
            plt.imshow(filtered_score, cmap='gray_r')
            plt.show()            
            break
            
        cv2.imwrite(f"{save_path}/region_scale_spot_{idx}.png", filtered_score)

def visualize_domains_spot_wise(spot_coord: np.ndarray,
                                spot_score: np.ndarray,
                                save_path: str,
                                feasible_domain: np.ndarray,
                                radius: int,
                                index: int = None):
    """
    Visualize domains with spot-wise embedding based on spot coordinates and region profiles.

    Args:
        spot_coord (numpy.ndarray): Array containing spot coordinates.
        spot_score (numpy.ndarray): Array containing spot scores or region profiles.
        save_path (str): Path where the visualizations will be saved.
        feasible_domain (numpy.ndarray): Array indicating feasible domains for masking the visualization.
        radius (int): The radius within which to find coordinates.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
    """

    # Get the range of the feasible domain
    row_range, col_range = feasible_domain.shape

    # Calculate relative indices within the spot radius
    relative_indices_within_radius = []
    for i in range(radius + 1):
        for j in range(radius + 1):
            if math.sqrt(i ** 2 + j ** 2) <= radius - 2:
                relative_indices_within_radius.extend([(i, j), (-i, j), (i, -j), (-i, -j)])
    relative_indices_within_radius = np.array(relative_indices_within_radius, dtype=int)

    # Visualize spot-wise embeddings
    for idx in range(spot_score.shape[1]):
        if index is not None: idx = index

        # Generate spot-wise visualization
        spotwise_score = np.zeros((row_range, col_range))
        for spot_index, (row_coord, col_coord) in enumerate(spot_coord):
            for row_offset, col_offset in relative_indices_within_radius:
                spot_row = int(row_coord) + row_offset
                spot_col = int(col_coord) + col_offset
                if 0 <= spot_row < row_range and 0 <= spot_col < col_range:
                    spotwise_score[spot_row, spot_col] = spot_score[spot_index, idx]

        # Normalize
        normalized_score = spotwise_score / spotwise_score.max() * 255

        # Apply feasible domains filtering
        filtered_score = normalized_score * feasible_domain

        # Visualize score of the specific index
        if index is not None:
            plt.imshow(filtered_score, cmap='gray_r')
            plt.show()
            break
            
        cv2.imwrite(f"{save_path}/region_scale_spot_{i}.png", filtered_score)


def visualize_deepfusenmf(all_score: np.ndarray,
                          save_path: str,
                          feasible_domain: np.ndarray,
                          cutoff_type: str = "absolute_value",
                          index: int = None):
    """
    Visualize domains for DeepFuseNMF embeddings.

    Args:
        all_score (numpy.ndarray): Array containing all scores.
        save_path (str): Path where the visualizations will be saved.
        feasible_domain (numpy.ndarray): Array indicating feasible domains for masking the visualization.
        cutoff_type (str, optional): The type of cutoff to be used. Defaults to "absolute_value".
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
    """

    # Create directory if not exists
    if index is None: os.makedirs(save_path, exist_ok=True)

    # Determine the pixel for max and min value
    feasible_pixel = np.where(feasible_domain == 1)

    # Visualize DeepFuseNMF embeddings for each dimension
    for idx in range(all_score.shape[0]):
        if index is not None: idx = index

        region_score = all_score[idx, :, :]
        if cutoff_type == "absolute_value":
            region_max = 1
        else:
            region_max = np.quantile(region_score[feasible_pixel[0], feasible_pixel[1]], 0.99)

        # Normalize
        normalized_score = region_score / region_max * 255

        # Apply feasible domains filtering
        filtered_score = normalized_score * feasible_domain

        # Visualize score of the specific index
        if index is not None:
            plt.imshow(filtered_score, cmap='gray_r')
            plt.show()
            break

        cv2.imwrite(f"{save_path}/region_scale_spot_{idx}.png", filtered_score)
