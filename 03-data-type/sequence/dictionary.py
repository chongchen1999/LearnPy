# Introduction to Dictionary
# A dictionary is a collection of key-value pairs, where each key is unique.

# Creating a dictionary
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Dictionary Example:")
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Accessing a value by its key
print(f"Alice's score: {student_scores['Alice']}")  # Output: 85

# Adding a new key-value pair
student_scores["David"] = 88
print("After adding David:", student_scores)

# Updating a value
student_scores["Alice"] = 90
print("After updating Alice's score:", student_scores)

# Deleting a key-value pair
del student_scores["Charlie"]
print("After removing Charlie:", student_scores)

print("\n")

# Introduction to Set
# A set is an unordered collection of unique elements.

# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
print("Set Example:")
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Adding an element
unique_numbers.add(6)
print("After adding 6:", unique_numbers)

# Removing an element
unique_numbers.remove(3)
print("After removing 3:", unique_numbers)

# Demonstrating uniqueness
unique_numbers.add(4)  # Adding 4 again doesn't change the set
print("After adding 4 again:", unique_numbers)

# Set operations
even_numbers = {2, 4, 6, 8}
print("Union:", unique_numbers.union(even_numbers))  # Combines both sets
print("Intersection:", unique_numbers.intersection(even_numbers))  # Common elements
print("Difference:", unique_numbers.difference(even_numbers))  # Elements in one but not the other
