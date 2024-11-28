a = [10, 20, 30]
a.append(40)

print(a)

b = a + [50, 60]

print(a)
print(b)

print(id(a))
print(id(b))