class Singleton:
    _instance = None  # Class-level private attribute to hold the single instance
    _initialized = False  # Track whether the instance has been initialized

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Check if the instance already exists
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not self._initialized:  # Prevent reinitialization
            self.value = value
            Singleton._initialized = True  # Mark as initialized

# Usage
singleton1 = Singleton("First Instance")
print(singleton1.value)  # Output: First Instance

singleton2 = Singleton("Second Instance")
print(singleton2.value)  # Output: First Instance (singleton is not reinitialized)

print(singleton1 is singleton2)  # Output: True
