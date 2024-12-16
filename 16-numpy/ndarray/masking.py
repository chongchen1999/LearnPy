import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Create a mask for values greater than 2
mask = arr > 2
print(mask)  # [False False  True  True  True]

# Filter values using the mask
filtered = arr[mask]
print(filtered)  # [3 4 5]
