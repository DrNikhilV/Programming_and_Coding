# Import necessary libraries
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate sample data
X = np.random.rand(100, 2)

# Create a K-Means clustering model with 3 clusters
model = KMeans(n_clusters=3)

# Fit the model to the data
model.fit(X)

# Get the cluster assignments for each data point
labels = model.labels_

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title("K-Means Clustering")
plt.show()
