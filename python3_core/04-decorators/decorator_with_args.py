def timefun(func):
    def wrapper_func(a, b):
        print("---1---")
        print(a, b)
        func(a, b)
        print("---2---")

    return wrapper_func

@timefun
def foo(a, b):
    print("---3---")
    print(a + b)
    print("---4---")

foo(10, 20)