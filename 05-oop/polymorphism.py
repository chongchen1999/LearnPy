class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet"

# Demonstrating polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating instances of the derived classes
bird = Bird()
elephant = Elephant()

# Calling the common method
animal_sound(bird)      # Output: Chirp
animal_sound(elephant)  # Output: Trumpet