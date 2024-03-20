import numpy as np
import math
from scipy.spatial.distance import cdist
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def query_batch(tree,
                query_points: np.ndarray) -> np.ndarray:
    """
    Query a batch of points using KDTree.

    Args:
        tree (scipy.spatial.kdtree.KDTree): An instance of KDTree.
        query_points (numpy.ndarray): Array containing the query points.

    Returns:
        nearest_indices (numpy.ndarray): Array containing the indices of the nearest neighbors.
    """

    return tree.query(query_points)[1]

def query_kdtree_parallel(tree,
                          query_points: np.ndarray,
                          workers: int = 1) -> np.ndarray:
    """
    Parallel query of KDTree to speed up the lookup process.

    Args:
        tree: An instance of KDTree.
        query_points (numpy.ndarray): Array containing the query points.
        workers (int): Number of workers to use for parallel querying.

    Returns:
        nearest_indices (numpy.ndarray): Array containing the indices of the nearest neighbors.
    """
    # Split query points into multiple batches for parallel querying
    split_indices = np.array_split(query_points, workers)

    # Use ProcessPoolExecutor for parallel querying
    with ProcessPoolExecutor(max_workers=workers) as executor:
        partial_query_batch = partial(query_batch, tree)
        futures = [executor.submit(partial_query_batch, points) for points in split_indices]
        results = [future.result() for future in futures]

    # Merge results
    nearest_indices = np.concatenate(results)
    return nearest_indices

def create_pseudo_spots(feasible_domain: np.ndarray,
                        radius: int,
                        seed: int = 123,
                        num_pseudo_spots: int = 10000,
                        num_split: int = 10) -> np.ndarray:
    """
    Create pseudo spots within a given feasible domain.

    Args:
        feasible_domains (numpy.ndarray): Array indicating the feasible domain for spots.
        num_pseudo_spots (int): The total number of pseudo spots to be created.
        num_splits (int): The number of segments to divide the creation process into.
        radius (int): The minimum distance to maintain between each spot.
        seed (int): Seed for random number generator.

    Returns:
        pseudo_spots (numpy.ndarray): Array containing the coordinates of the pseudo spots.
    """

    np.random.seed(seed)
    spots_per_split = math.ceil(num_pseudo_spots / num_split)

    # Prepare the initial feasible domain by excluding the edges
    feasible_domains_current = feasible_domain.copy()
    feasible_domains_current[:radius, :] = 0
    feasible_domains_current[-radius:, :] = 0
    feasible_domains_current[:, :radius] = 0
    feasible_domains_current[:, -radius:] = 0

    row_indices, col_indices = [], []
    for _ in range(num_split):
        feasible_indices = np.where(feasible_domains_current == 1)
        num_available_spots = feasible_indices[0].shape[0]

        if num_available_spots > 0:
            chosen_indices = np.sort(
                np.random.choice(num_available_spots, size=min(spots_per_split, num_available_spots),
                                 replace=False))
            row_indices.extend(feasible_indices[0][chosen_indices])
            col_indices.extend(feasible_indices[1][chosen_indices])

            # Update the feasible domain after selecting each spot
            for index in chosen_indices:
                row, col = feasible_indices[0][index], feasible_indices[1][index]
                row_start, row_end = max(0, row - radius), min(feasible_domains_current.shape[0], row + radius + 1)
                col_start, col_end = max(0, col - radius), min(feasible_domains_current.shape[1], col + radius + 1)
                feasible_domains_current[row_start:row_end, col_start:col_end] = 0

    # Create a DataFrame from the pseudo spot coordinates
    pseudo_spots = np.vstack((row_indices, col_indices)).T - 1

    return pseudo_spots

def construct_adjacency_matrix(spot_coord: np.ndarray,
                               spot_embeddings: np.ndarray,
                               num_real_spots: int,
                               num_neighbors: int = 20) -> np.ndarray:
    """
    Construct the adjacency matrix for the graph.

    Args:
        spot_coord (numpy.ndarray): Array containing the coordinates of the spots.
        spot_embeddings (numpy.ndarray): Array containing the embeddings of the spots.
        num_real_spots (int): The number of real spots in the dataset.
        num_neighbors (int): The number of neighbors to consider for each spot.

    Returns:
        adjacency_matrix (numpy.ndarray): The adjacency matrix for the graph.
    """

    num_all_spots = spot_coord.shape[0]
    num_pseudo_spots = num_all_spots - num_real_spots

    # Calculate the proportional number of pseudo neighbors
    num_pseudo_neighbors = math.ceil(num_pseudo_spots / num_real_spots * num_neighbors)

    # Calculate distances and correlation
    distances = cdist(spot_coord, spot_coord, 'euclidean')
    correlation_matrix = np.corrcoef(spot_embeddings)

    # Initialize adjacency matrix
    adjacency_matrix = np.zeros((num_all_spots, num_all_spots))

    # Define ranges for real and pseudo spots
    real_range = np.arange(num_real_spots)
    pseudo_range = np.arange(num_real_spots, num_all_spots)

    for index in range(num_all_spots):
        # Find nearest neighbors based on distance
        real_indices = real_range[np.argsort(distances[index, real_range])[:num_neighbors]]
        pseudo_indices = pseudo_range[np.argsort(distances[index, pseudo_range])[:num_pseudo_neighbors]]

        # Select top 2 correlated neighbors from real and pseudo spots
        top_real_neighbors = real_indices[np.argsort(-correlation_matrix[index, real_indices])[:2]]
        top_pseudo_neighbors = pseudo_indices[np.argsort(-correlation_matrix[index, pseudo_indices])[:2]]

        # Combine selections and update adjacency matrix
        selected_neighbors = np.hstack((top_real_neighbors, top_pseudo_neighbors))
        adjacency_matrix[index, selected_neighbors] = 0.25

    return adjacency_matrix
