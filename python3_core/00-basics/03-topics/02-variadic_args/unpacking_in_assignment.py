a, *b, c = [1, 2, 3, 4]
print(a)  # 1
print(b)  # [2, 3]
print(c)  # 4

# Dictionary merging
dict1 = {"x": 1, "y": 2}
dict2 = {"z": 3}
merged = {**dict1, **dict2}
print(merged)  # {'x': 1, 'y': 2, 'z': 3}
