class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

# Create an instance of Adder
add5 = Adder(5)

# Use the instance as a function
result = add5(10)  # Equivalent to add5.__call__(10)
print(result)  # Output: 15