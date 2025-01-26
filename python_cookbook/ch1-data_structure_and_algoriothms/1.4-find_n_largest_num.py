import heapq

# Example 1: Working with a List of Numbers
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# Find the 3 largest numbers
print(heapq.nlargest(3, nums))  # Output: [42, 37, 23]

# Find the 3 smallest numbers
print(heapq.nsmallest(3, nums))  # Output: [-4, 1, 2]


# Example 2: Working with a List of Dictionaries
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# Find the 3 cheapest stocks (smallest 'price')
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
# Output: [{'name': 'YHOO', 'shares': 45, 'price': 16.35},
#          {'name': 'FB', 'shares': 200, 'price': 21.09},
#          {'name': 'HPQ', 'shares': 35, 'price': 31.75}]

# Find the 3 most expensive stocks (largest 'price')
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
# Output: [{'name': 'AAPL', 'shares': 50, 'price': 543.22},
#          {'name': 'ACME', 'shares': 75, 'price': 115.65},
#          {'name': 'IBM', 'shares': 100, 'price': 91.1}]