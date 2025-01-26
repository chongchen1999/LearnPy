nums = [11, 22, 33, 44]

print(type(nums))

nums_iter = iter(nums)
print(type(nums_iter))

for num in nums_iter:
    print(num)