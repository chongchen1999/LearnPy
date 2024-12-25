# Refers to variables in the nearest enclosing scope.

def outer_function():
    x = 10  # Enclosing variable (non-local)

    def inner_function():
        nonlocal x  # Declare 'x' as non-local
        x += 5  # Modify the enclosing variable
        print(f"Inside inner_function, non-local x: {x}")

    inner_function()
    print(f"Inside outer_function, modified x: {x}")

outer_function()
