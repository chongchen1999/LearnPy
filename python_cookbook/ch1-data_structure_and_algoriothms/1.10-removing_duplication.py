def simple_generator():
    i = 0
    for i in range(10):
        yield i
        i += 1

a = list(simple_generator())
print(a)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))  # Output: [1, 5, 2, 9, 10]


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))  
# Output: [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

print(list(dedupe(a, key=lambda d: d['x'])))  
# Output: [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

with open('data/somefile.txt', 'r') as f:
    for line in dedupe(f):
        print(line, end='')
