# In python, a variable holds a reference to an object.

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

a.append(4)
print(a)
print(b) # Both a and b are now [1, 2, 3, 4]