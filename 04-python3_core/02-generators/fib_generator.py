class FibGenerator:
    def __init__(self, n = 100, a = 1, b = 1):
        self.n = n
        self.i = 0
        self.a = a
        self.b = b
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration
        self.i += 1
        if self.i == 1:
            return self.a
        elif self.i == 2:
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            return self.b
    
if __name__ == '__main__':
    fib = FibGenerator(10)
    for i in fib:
        print(i, end = ' ')
    print()

    fib = FibGenerator(100, 156, 2365441)
    for i in fib:
        print(i, end = ' ')
    print()

    time.sleep(1)