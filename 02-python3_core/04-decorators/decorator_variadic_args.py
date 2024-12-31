def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print('Function name: ', func.__name__)
        print('Arguments: ', args)
        print('Keyword arguments: ', kwargs)
        return func(*args, **kwargs)
    
    return wrapper

@universal_decorator
def a(num):
    print('a: ', num)
    return 100

@universal_decorator
def b(num, num2):
    print('b: ', num, num2)

@universal_decorator
def c(num, num2, num3):
    print('c: ', num, num2, num3)

print(a(1))
b(2, 3)
c(4, 5, 6)
