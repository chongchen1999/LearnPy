def decorator_return_value(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator_return_value
def my_function(num):
    print(f"Number: {num}")
    return num * 2

@decorator_return_value
def my_function2(num, num2):
    print(f"Number: {num} and {num2}")
    return num * num2

print(my_function(5))
print(my_function2(5, 10))
