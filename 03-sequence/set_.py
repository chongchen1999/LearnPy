# Set operations
numbers = {1, 2, 3, 4}
numbers.add(5)  # Add an element
numbers.discard(2)  # Remove an element
duplicates = {1, 2, 2, 3, 3}
unique_numbers = set(duplicates)  # Remove duplicates
print("Set:", numbers)  # Output: {1, 3, 4, 5}
print("Unique Numbers:", unique_numbers)  # Output: {1, 2, 3}
