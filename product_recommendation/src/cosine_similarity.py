import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item interaction matrix (rows are users, columns are items)
# Each value could represent, for example, the number of times a user bought an item
user_item_matrix = np.array([
    [3, 0, 2, 0],
    [1, 1, 0, 1],
    [0, 2, 3, 0],
    [2, 0, 1, 3]
])

# 1. Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# 2. Compute cosine similarity between items
item_similarity = cosine_similarity(user_item_matrix.T)  # Transpose to get item similarity

print("User Similarity Matrix:\n", user_similarity)
print("\nItem Similarity Matrix:\n", item_similarity)
