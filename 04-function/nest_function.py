def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Alice"))
# Output: Hello, Alice!
