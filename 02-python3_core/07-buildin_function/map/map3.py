def f(x, y):
    return x, y

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
l3 = map(f, l1, l2)
print(list(l3))
print("----------------")
print(list(l3))

for temp in list(l3):
    print(temp)