class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorating function")
        self.func(*args, **kwargs)

@Test
def test_func():
    print("Test function")

test_func()