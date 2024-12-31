# Define the decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is about to be called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

# Use the decorator
@logger
def add(a, b):
    return a + b

# Call the decorated function
print(add(5, 3))
