class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return "Person's name is {0}".format(self.name)

p = Person("John")
print(p)