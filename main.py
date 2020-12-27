import matplotlib.pyplot as plt
# from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import numpy as np


features, true_labels = make_blobs(
    n_samples=200, centers=3, cluster_std=2.75, random_state=42
)

# print(features[:5])

# print(true_labels[:5])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# print(scaled_features[:5])

kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
)

kmeans.fit(scaled_features)

# The lowest SSE value
# print(kmeans.inertia_)


# The number of iterations required to converge
# print(kmeans.n_iter_)

# print(kmeans.labels_[:5])

new_data = np.array([2.2, 0.5])

# Final locations of the centroid
centroids = kmeans.cluster_centers_


# Calculate distance
diff = centroids - new_data

# Calculating Euclidean distance
dist = np.sqrt(np.sum(diff**2, axis=-1))

print('Closest cluster: ',np.argmin(dist))
closest_centroid = centroids[np.argmin(dist),]
print('Closest centroid: ',closest_centroid)
