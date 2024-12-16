import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Basic aggregations
print(np.sum(arr))  # 15
print(np.mean(arr)) # 3.0
print(np.min(arr))  # 1
print(np.max(arr))  # 5

# Aggregation over specific axes
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(matrix, axis=0))  # Sum of each column -> [5 7 9]
print(np.sum(matrix, axis=1))  # Sum of each row -> [ 6 15]
