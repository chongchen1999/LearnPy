nums = [55, 66, 33, 44]

for temp in nums:
    print(temp)

name = "Python"
for temp in name:
    print(temp)

for x in {11:22, "String": 3, (1, 2, "string_"): 3}:
    print(x)


print("-" * 50)
list = [1, 2, 3, 4, 5]
list_iter = iter(list)
while True:
    try:
        print(next(list_iter))
    except StopIteration:
        break