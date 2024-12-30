def generator_test():
    while True:
        print("---1---")
        num = yield 100
        print("---2---", "num =", num)

g = generator_test()

print(g.__next__())
# print(next(g))
# print(next(g))

print(g.send(200))
print(g.send(300))