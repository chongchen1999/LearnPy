import numpy as np
import math

a = np.arange(10)
print(a)
print(a.shape)
print(type(a))

a = [3, 5, 6, 8]
print(id(a))
print(type(a))

for i in range(len(a)):
    a[i] = math.sqrt(a[i])

print(a)
print(id(a))
print(type(a))