def create():
    pos = [0, 0]
    def player(direction, step):
        pos[0], pos[1] = pos[0] + direction[0] * step, pos[1] + direction[1] * step
        return pos
    
    return player

player = create()
print(player([1, 0], 10))
print(player([0, 1], 20))
print(player([-1, 0], 10))