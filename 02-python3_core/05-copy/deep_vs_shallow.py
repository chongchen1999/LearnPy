"""
This script explains the concepts of shallow copy and deep copy in Python, as well as the difference between the comparison operators `==` and `is`.
"""

import copy

# Example for shallow copy
print("\n=== Shallow Copy Example ===")
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

# Modifying the copied list
shallow_copied_list[0][0] = 99

print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

# Explanation of shallow copy
print("\nExplanation: In a shallow copy, only the outer object is duplicated. Inner objects are still references to the same objects in memory.")

# Example for deep copy
print("\n=== Deep Copy Example ===")
deeper_copied_list = copy.deepcopy(original_list)

# Modifying the deeply copied list
deeper_copied_list[0][0] = 42

print("Original List:", original_list)
print("Deep Copied List:", deeper_copied_list)

# Explanation of deep copy
print("\nExplanation: In a deep copy, both the outer object and all nested objects are recursively duplicated. Changes to the copied structure do not affect the original.")

# == vs is comparison
print("\n=== Comparison Operators: == and is ===")
a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)  # True, because their contents are equal.
print("a is b:", a is b)  # False, because they are different objects in memory.

c = a
print("a is c:", a is c)  # True, because both variables reference the same object.

# Explanation of == and is
print("\nExplanation:")
print("- The `==` operator checks for value equality. It verifies if two objects have the same contents.")
print("- The `is` operator checks for identity equality. It verifies if two variables point to the same object in memory.")
