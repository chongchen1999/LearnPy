def divide_numbers(a, b):
    try:
        # Code that might raise an exception
        result = a / b
    except ZeroDivisionError as e:
        # Handle specific exception
        print("Error: Division by zero is not allowed.")
        print(f"Exception details: {e}")
    except TypeError as e:
        # Handle another specific exception
        print("Error: Invalid input type. Please enter numbers.")
        print(f"Exception details: {e}")
    else:
        # Code to execute if no exception occurs
        print(f"The result is: {result}")
    finally:
        # Code that executes no matter what
        print("Execution complete.")

def use_variable_in_finally():
    try:
        print("In try block...")
        x = 10  # Declare a variable
        result = x / 2  # Successful operation
        print(f"Result in try: {result}")
    except Exception as e:
        print("Exception occurred:", e)
    finally:
        # x is accessible here because it was successfully declared in the try block
        print("In finally block...")
        try:
            print(f"Value of x in finally: {result}")
        except NameError:
            print("result is not accessible.")

# Test the function
divide_numbers(10, 2)   # Normal case
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, 'a') # Invalid type

use_variable_in_finally()
