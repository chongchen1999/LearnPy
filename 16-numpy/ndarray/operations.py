import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(a + b)  # [5 7 9]
print(a * b)  # [4 10 18]
print(a ** 2) # [1 4 9]

# Universal functions
print(np.sqrt(a))  # [1. 1.41421356 1.73205081]
print(np.exp(a))   # [  2.71828183   7.3890561   20.08553692]
