import copy

# Original nested list
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copied_list = copy.copy(original_list)

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the original nested list
original_list[0][0] = 99
original_list[0] = [7, 8, 9]

# Print results
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)
