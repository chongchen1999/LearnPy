import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Basic slicing
print(arr[1:4])  # [20 30 40]

# 2D array indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])  # Element at row 1, col 2 -> 6
print(matrix[:, 1])  # Second column -> [2 5 8]
print(matrix[1, :])  # Second row -> [4 5 6]
