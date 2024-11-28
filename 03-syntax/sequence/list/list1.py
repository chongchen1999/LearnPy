def list_basic():
    w = range(1, 10)
    a = list(range(1, 10))
    b = list(range(3, 15, 3))

    print(w)
    print(a)
    print(b)

    print(type(w), type(a), type(b))


a = [x * 2 for x in range(20) if x % 3 == 1]
print(a)

a[0] = 0
print(a)