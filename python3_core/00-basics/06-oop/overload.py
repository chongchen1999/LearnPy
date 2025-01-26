class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return f"{self.name} {other.name}"
        else:
            return "Not a person"
    
    def __mul__(self, other):
        if isinstance(other, int):
            return self.name * other
        else:
            return "Not an integer"

p1 = Person("John")
p2 = Person("Doe")
print(p1 + p2)
print(p1 * 3)

print(p1.__dict__)
print(dir(p1))