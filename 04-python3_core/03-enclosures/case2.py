def line_conf(a, b):
    def line(x):
        return a * x + b
    
    def line2(x):
        return 2 * a * x + 2 * b
    return line, line2

line1 = line_conf(1, 1)
print(type(line1[0]))
