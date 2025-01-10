from collections.abc import Iterable
from collections.abc import Iterator

a = range(10)
print(a)
print(type(a))

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))