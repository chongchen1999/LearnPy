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
gen2 = (x for x in range(5))
print(type(gen))
print(type(gen2))

for x in gen:
    print(x)