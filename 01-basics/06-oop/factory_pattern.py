from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Subclasses implementing the abstract method
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory function to create objects
def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
animal1 = animal_factory("dog")
print(animal1.speak())  # Output: Woof!

animal2 = animal_factory("cat")
print(animal2.speak())  # Output: Meow!
