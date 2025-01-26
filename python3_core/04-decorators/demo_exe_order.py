def A(func):
    print("------0------")
    def B():
        print("------1------")
        func()
        print("------2------")

    print("------3------")
    return B

@A
def say_hello():
    print("Hello")

