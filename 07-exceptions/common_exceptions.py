# Common Exception Handling Examples in Python

# 1. Handling File Not Found
def handle_file_not_found():
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    else:
        print("File content:")
        print(content)
        file.close()
    finally:
        print("Execution complete.")

# 2. Division by Zero
def handle_division_by_zero():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")
    except ValueError as e:
        print("Error: Please enter a valid number.")
    else:
        print(f"The result is: {result}")
    finally:
        print("Program execution complete.")

# 3. Type Mismatch
def handle_type_mismatch():
    try:
        num_list = [1, 2, 3]
        print(num_list[5])  # IndexError
    except IndexError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Handled type-related exceptions.")

# 4. Key Not Found in Dictionary
def handle_key_error():
    try:
        data = {"name": "Alice", "age": 25}
        print(data["gender"])
    except KeyError as e:
        print(f"Error: Key {e} not found in the dictionary.")

# 5. Import Error
def handle_import_error():
    try:
        import non_existent_module
    except ImportError as e:
        print(f"Error: {e}")

# 6. Handling Multiple Exceptions
def handle_multiple_exceptions():
    try:
        value = int("not_a_number")  # ValueError
        result = 10 / 0  # ZeroDivisionError (won't reach this line)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

# 7. Custom Exception Handling
class CustomError(Exception):
    pass

def handle_custom_exception():
    try:
        raise CustomError("This is a custom exception.")
    except CustomError as e:
        print(f"Caught custom exception: {e}")

# 8. Cleaning Resources with finally
def handle_resource_cleanup():
    try:
        file = open("example.txt", "w")
        file.write("Hello, world!")
    except IOError as e:
        print(f"File operation failed: {e}")
    finally:
        file.close()
        print("File closed.")

# 9. Handling OS Errors
def handle_os_errors():
    import os
    try:
        os.remove("non_existent_file.txt")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Permission denied. {e}")

# 10. Nested Try-Except
def handle_nested_exceptions():
    try:
        try:
            num = int(input("Enter a number: "))
            result = 10 / num
        except ZeroDivisionError as e:
            print("Inner error: Division by zero.")
    except ValueError as e:
        print("Outer error: Invalid input.")
    finally:
        print("Nested exception handling complete.")

# Main function to run all examples
if __name__ == "__main__":
    print("Example 1: Handling File Not Found")
    handle_file_not_found()
    print("\nExample 2: Division by Zero")
    handle_division_by_zero()
    print("\nExample 3: Type Mismatch")
    handle_type_mismatch()
    print("\nExample 4: Key Not Found in Dictionary")
    handle_key_error()
    print("\nExample 5: Import Error")
    handle_import_error()
    print("\nExample 6: Handling Multiple Exceptions")
    handle_multiple_exceptions()
    print("\nExample 7: Custom Exception Handling")
    handle_custom_exception()
    print("\nExample 8: Cleaning Resources with finally")
    handle_resource_cleanup()
    print("\nExample 9: Handling OS Errors")
    handle_os_errors()
    print("\nExample 10: Nested Try-Except")
    handle_nested_exceptions()
