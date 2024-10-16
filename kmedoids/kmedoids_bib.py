# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn.metrics import adjusted_rand_score

# Custom data points
#X = np.array([[0, 1], [2, 3], [3, 4], [8, 7], [9, 6], [7, 8]])
X = np.array([
    [1.0, 2.0], [1.5, 2.5], [1.2, 1.8],  # Cluster 0
    [2.0, 3.0], [2.5, 2.7], [2.3, 3.2],  # Cluster 0 (overlapping with cluster 1)
    [3.5, 3.5], [4.0, 4.0], [3.8, 3.8],  # Cluster 1
    [5.0, 5.0], [5.5, 5.2], [4.9, 5.1],   # Cluster 1 (but overlapping with cluster 2)
    [7.0, 8.0], [7.5, 7.8], [6.8, 8.1],  # Cluster 2
])

#true_labels = np.array([0, 0, 0, 1, 1, 1])
true_labels = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2])

# Number of clusters
n_clusters = 3

# Initialize and fit K-Medoids
kmedoids = KMedoids(n_clusters=n_clusters, random_state=42)
kmedoids.fit(X)

def monte_carlo_experiment(data, true_labels, k, num_trials):
    rand_indices = []

    for trial in range(num_trials):
        predicted_labels = kmedoids.predict(X)
        rand_idx = adjusted_rand_score(true_labels, predicted_labels)
        #print(f"Adjusted Rand Index (ARI): {rand_idx:.2f}")
        rand_indices.append(rand_idx)

    mean_rand_index = np.mean(rand_indices)
    std_rand_index = np.std(rand_indices)
    return mean_rand_index, std_rand_index

num_trials = 100
k = 3
mean_rand_idx, std_rand_idx = monte_carlo_experiment(data, true_labels, k, num_trials)

print(f"Monte Carlo K-Medoids Clustering Results ({num_trials} trials)")
print(f"Mean Rand Index: {mean_rand_idx:.4f}")
print(f"Standard Deviation of Rand Index: {std_rand_idx:.4f}")
