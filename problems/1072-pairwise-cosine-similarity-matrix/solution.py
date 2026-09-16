import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    norms = np.maximum(np.linalg.norm(X, axis=1, keepdims=True),1e-6)
    x_norm = X/norms

    return x_norm @ x_norm.T