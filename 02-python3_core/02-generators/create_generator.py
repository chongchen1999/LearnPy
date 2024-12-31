# nums = [x for x in range(10)]
# print(type(nums))
# print(nums)

nums2 = (x for x in range(20))
print(type(nums2))
print(nums2)

for num in nums2:
    print(num, end=' ')
print()