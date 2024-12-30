import random

l = [random.randint(-100, 100) for _ in range(10)]
print(l)

# l = [x for x in l if x >= 0]
# print(l)

filter(lambda x: x >= 0, l)