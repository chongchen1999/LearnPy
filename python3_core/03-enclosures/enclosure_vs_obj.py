def line(k = 1, b = 2):
    def f(x):
        print(x, k * x + b)
    
    return f

line1 = line(3, 4)
line1(5)

