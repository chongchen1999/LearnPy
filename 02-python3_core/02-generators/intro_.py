def generate_point():
    point_list = []

    i = 0
    x = 0

    while i < 5:
        y = 2 * x + 1
        point_list.append((x, y))
        x = y
        i += 1

    print(point_list)

if __name__ == '__main__':
    generate_point()