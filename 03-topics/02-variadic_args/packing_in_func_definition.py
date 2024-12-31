def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Charlie", age=40)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Charlie', 'age': 40}
