def test():
    pass

a = test
print(id(a))
print(id(test))

a = [11, 22, 33]
b = a
a.append(44)
print(a)
print(b)

def add(temp):
    print(id(temp))
    temp.append(44)
    print(temp)

a = [11, 22, 33]
print(id(a))
add(a)
print(a)