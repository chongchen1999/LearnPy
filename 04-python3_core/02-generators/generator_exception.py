def fib_generator():
    a, b = 0, 1
    yield a

    b, a = a + b, b
    yield a

    b, a = a + b, b
    yield a

    b, a = a + b, b
    yield a

    print('This is the last line of the generator function')
    return 'Done'

gen = fib_generator()

for x in gen:
    print(x)