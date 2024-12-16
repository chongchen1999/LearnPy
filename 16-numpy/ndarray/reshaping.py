import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Reshaping to 2x3
reshaped = arr.reshape((2, 3))
print(reshaped)
# [[1 2 3]
#  [4 5 6]]

# Transposing
transposed = reshaped.T
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
