import numpy as np

# 1D array from a Python list
arr1 = np.array([1, 2, 3, 4])
print(arr1)  # [1 2 3 4]

# 2D array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
# [[1 2]
#  [3 4]]

# Arrays with specific values
zeros = np.zeros((2, 3))       # 2x3 matrix of zeros
ones = np.ones((2, 3))         # 2x3 matrix of ones
identity = np.eye(3)           # 3x3 identity matrix
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1

print(zeros)
print(ones)
print(identity)
print(linspace)