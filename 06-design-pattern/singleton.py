class Singleton:
    _instance = None  # Class-level private attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Check if the instance already exists
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
