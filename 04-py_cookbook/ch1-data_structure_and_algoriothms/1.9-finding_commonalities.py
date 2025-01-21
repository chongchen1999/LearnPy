a = { 'x': 1, 'y': 2, 'z': 3 }
b = { 'w': 10, 'x': 11, 'y': 2 }

common_keys = a.keys() & b.keys()
print(common_keys)  # Output: {'x', 'y'}

keys_in_a_not_in_b = a.keys() - b.keys()
print(keys_in_a_not_in_b)  # Output: {'z'}

common_items = a.items() & b.items()
print(common_items)  # Output: {('y', 2)}

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # Output: {'x': 1, 'y': 2}