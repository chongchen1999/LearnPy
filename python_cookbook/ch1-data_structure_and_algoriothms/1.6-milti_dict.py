from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 4), ('a', 3)]

# Using defaultdict
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)  # Output: defaultdict(<class 'list'>, {'a': [1, 2, 3], 'b': [4]})