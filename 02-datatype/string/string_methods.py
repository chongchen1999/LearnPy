# Define the string variable
a = "I am learning Python programming"

# 1. len(a): Get the length of the string
print("Length of the string:", len(a))  # Output: 33

# 2. a.startswith('I am'): Check if the string starts with 'I am'
print("Does the string start with 'I am'?", a.startswith('I am'))  # Output: True
print("Does the string start with 'learning'?", a.startswith('learning'))  # Output: False

# 3. a.endswith('programming'): Check if the string ends with 'programming'
print("Does the string end with 'programming'?", a.endswith('programming'))  # Output: True
print("Does the string end with 'Python'?", a.endswith('Python'))  # Output: False

# 4. a.find('Python'): Find the first occurrence of 'Python'
print("Index of 'Python':", a.find('Python'))  # Output: 14
print("Index of 'Java':", a.find('Java'))  # Output: -1 (not found)

# 5. a.rfind('a'): Find the last occurrence of 'a'
print("Last index of 'a':", a.rfind('a'))  # Output: 5
print("Last index of 'z':", a.rfind('z'))  # Output: -1 (not found)

# 6. a.count('learning'): Count the occurrences of 'learning'
print("Count of 'learning':", a.count('learning'))  # Output: 1
print("Count of 'Python':", a.count('Python'))  # Output: 1
print("Count of 'Java':", a.count('Java'))  # Output: 0

# 7. a.isalnum(): Check if all characters in the string are alphanumeric
b = "Python123"  # Only letters and numbers
c = "Python 123"  # Contains a space
d = "Python@123"  # Contains a special character
print("Is 'Python123' alphanumeric?", b.isalnum())  # Output: True
print("Is 'Python 123' alphanumeric?", c.isalnum())  # Output: False
print("Is 'Python@123' alphanumeric?", d.isalnum())  # Output: False
