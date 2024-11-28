# file: string_format_examples.py

# 1. Basic Formatting with Positional Placeholders
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.

# 2. Positional Indexing
print("{1} is learning {0}".format("Python", "Bob"))
# Output: Bob is learning Python

# 3. Keyword Placeholders
print("My name is {name} and I am {age} years old.".format(name="Alice", age=25))
# Output: My name is Alice and I am 25 years old.

# 4. Formatting Numbers
# Decimal places
print("Pi is approximately {:.2f}".format(3.14159))
# Output: Pi is approximately 3.14

# Integer padding with leading zeros
print("Number: {:05d}".format(42))
# Output: Number: 00042

# 5. Aligning Text
# Left-align, right-align, and center
print("{:<10} | {:>10} | {:^10}".format("Left", "Right", "Center"))
# Output:
# Left       |      Right |   Center   

# 6. Combining Named and Positional Arguments
print("The {animal} jumped over the {0}.".format("fence", animal="fox"))
# Output: The fox jumped over the fence.

# 7. Using f-Strings (Modern Alternative to `format()`)
# Basic example
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.

# Formatting numbers with f-strings
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")
# Output: Pi is approximately 3.14

# Integer padding with f-strings
number = 42
print(f"Number: {number:05d}")
# Output: Number: 00042

# Aligning text with f-strings
print(f"{'Left':<10} | {'Right':>10} | {'Center':^10}")
# Output:
# Left       |      Right |   Center   
