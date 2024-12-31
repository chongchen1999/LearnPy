def foo():
    print("foo() called")

foo = lambda x : x + 1

def make_pencil(color):
    def write(content):
        print(f"Writing \"{content}\" in \"{color}\" pencil")

    return write

red_pencil = make_pencil("red")
blue_pencil = make_pencil("blue")

red_pencil("I am red")
blue_pencil("I am blue")
