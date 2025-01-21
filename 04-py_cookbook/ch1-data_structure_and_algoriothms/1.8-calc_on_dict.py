prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]


min_key = min(prices, key=lambda k: prices[k])  # Returns 'FB'
max_key = max(prices, key=lambda k: prices[k])  # Returns 'AAPL'
print(min_key)
print(max_key)


zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
a, b = zip((1, 'a'), (2, 'b'), (3, 'c'))
print(a)  # (1, 2, 3)
print(b)  # ('a', 'b', 'c')

