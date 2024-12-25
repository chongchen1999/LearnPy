# Dynamically import the 'math' module using importlib
import importlib

module_name = "math"
math_module = importlib.import_module(module_name)

# Using the dynamically imported module
result = math_module.sqrt(25)
print("Square root of 25 is:", result)  # Output: 5.0
