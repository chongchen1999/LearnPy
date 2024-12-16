import numpy as np

matrix = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])

# Matrix multiplication
product = np.dot(matrix, vector)
print(product)  # [17 39]

# Determinant
print(np.linalg.det(matrix))  # -2.0

# Eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(matrix)
print(eigvals)  # Eigenvalues
print(eigvecs)  # Eigenvectors
