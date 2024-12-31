def counter(start = 0):
    def increment():
        nonlocal start
        start += 1
        return start
    
    return increment

c1 = counter(5)
print(c1())
print(c1())