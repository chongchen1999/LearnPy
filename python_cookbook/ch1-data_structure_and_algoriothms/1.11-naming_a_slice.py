record = '....................100 .......513.25 ..........'

# Correctly slice and print the portions
print(record[20:23])  # Output: '100'
print(record[31:37])  # Output: '513.25'

# Calculate cost
cost = int(record[20:23]) * float(record[31:37])
print("Cost:", cost)

# Using `slice` objects
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print("Cost using slices:", cost)

# Demonstrating slice attributes
a = slice(10, 50, 2)
print(a.start)  # Output: 10
print(a.stop)   # Output: 50
print(a.step)   # Output: 2

# Using `slice.indices` for bounds-safe slicing
s = 'HelloWorld'
a = slice(5, 15, 2)
print(a.indices(len(s)))  # Output: (10, 10, 2) — corrected

for i in range(*a.indices(len(s))):
    print(s[i])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])  # Output: [2, 3]

items[a] = [10, 11]
print(items)  # Output: [0, 1, 10, 11, 4, 5, 6]

del items[a]
print(items)  # Output: [0, 1, 4, 5, 6]