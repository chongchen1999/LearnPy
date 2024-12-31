# Packing multiple values into a tuple
a, b, c = 1, 2, 3  # This assigns values directly (no packing here)
packed = (a, b, c)  # Packing the variables into a tuple
print(packed)  # Output: (1, 2, 3)
print(type(packed))  # Output: <class 'tuple'>

# Packing into a list
values = [1, 2, 3, 4, 5]
print(values)  # Output: [1, 2, 3, 4, 5]
print(type(values))  # Output: <class 'list'>

# Packing into a dictionary
packed_dict = {"x": 1, "y": 2, "z": 3}
print(packed_dict)  # Output: {'x': 1, 'y': 2, 'z': 3}
print(type(packed_dict))  # Output: <class 'dict'>