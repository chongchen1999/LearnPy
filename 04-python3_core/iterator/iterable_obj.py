for x in [55, 77]:
    print(x)

for x in {33: 44, 55: 66}:
    print(x)

from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({1, 2, 3}, Iterable))
print(isinstance({1: 2, 3: 4}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

for x in {11:22, "String":3}:
    print(x)