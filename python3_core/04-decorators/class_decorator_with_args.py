class Test:
    def __init__(self, num):
        print(f"Test class initialized with {num}")
        self.num = num

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Wrapper executed with {self.num}")
            return func(*args, **kwargs)
        return wrapper
    
@Test(10)
def test_func(num):
    print("test function called")
    print(f"Number: {num}")

# test_func(233)
