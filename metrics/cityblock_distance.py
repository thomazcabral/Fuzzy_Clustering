import numpy as np
from scipy.spatial.distance import pdist, squareform

X = np.array([
    [1, 2],
    [2, 4]
])

condensed_dist = pdist(X, metric='cityblock')

distance_matrix = squareform(condensed_dist)

print(distance_matrix)