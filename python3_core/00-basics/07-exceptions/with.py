# File: with_statement_examples.py

# Example 1: Using 'with' for file handling
def file_handling_example():
    print("\n--- File Handling Example ---")
    # Without 'with' statement
    file = open("example.txt", "w")
    try:
        file.write("Hello, World!")
    finally:
        file.close()

    # With 'with' statement
    with open("example.txt", "w") as file:
        file.write("Hello, Python World!")  # File is automatically closed after the block

    print("Check 'example.txt' for content.")

# Example 2: Custom context manager
class CustomManager:
    def __enter__(self):
        print("Entering the context")
        return "You are inside the context"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        return True  # Suppress exceptions if needed

def custom_context_manager_example():
    print("\n--- Custom Context Manager Example ---")
    with CustomManager() as message:
        print(message)
        # Uncomment the next line to see exception handling
        # raise ValueError("Something went wrong!")

# Main function to call all examples
def main():
    file_handling_example()
    custom_context_manager_example()

if __name__ == "__main__":
    main()
