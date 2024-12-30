def fib_generator():
    num1 = 1
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2

fib = fib_generator()
print(fib)
print(type(fib_generator))

for i in range(10):
    print(next(fib), end=' ')