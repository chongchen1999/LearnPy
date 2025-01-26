def greet(x, y, name, age):
    print(f"Name: {name}, Age: {age}")

args = ("Alice", 30, 10, 20)
greet(*args)  # Equivalent to greet("Alice", 30)

kwargs = {"name": "Bob", "age": 25}
greet(10, 20, **kwargs)  # Equivalent to greet(name="Bob", age=25)
# greet(10, 20, name="Bob", age=25)
