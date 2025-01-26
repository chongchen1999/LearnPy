def point_generator(x = 0, k = 2, b = 1):
    while True:
        y = k * x + b
        received = yield (x, y)
        if received:
            x, k, b = received
        else:
            x = y

point_gen = point_generator()

for i in range(10):
    print(next(point_gen))

print('---')
print(point_gen.send((10000, 233, 666)))