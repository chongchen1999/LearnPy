class PointGenerator:
    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        y = 2 * self.x + 1
        ret = (self.x, y)
        self.x = y
        return ret


if __name__ == '__main__':
    point_gen = PointGenerator()
    for i in range(20): 
        point = next(point_gen) 
        print(f"{i}: {point}")