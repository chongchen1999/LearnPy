numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a, ' ', type(a))
print(b, ' ', type(b))
print(c, ' ', type(c))

numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers
print(a, ' ', type(a))
print(b, ' ', type(b))
print(c, ' ', type(c))

numbers = {1, 2, 3, 4, 5}
a0, *a = numbers
print(a, ' ', type(a))