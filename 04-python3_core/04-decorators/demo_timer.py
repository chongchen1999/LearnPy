import time

# Define the decorator
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Use the decorator
@execution_time
def slow_function():
    time.sleep(2)  # Simulate a slow operation
    return "Finished"

# Call the decorated function
print(slow_function())
