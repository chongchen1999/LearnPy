try:
    print("step 1")
    a = 1 / 0
    print("step 2")
except ZeroDivisionError as e:
    print(e)
    print("step 3")
    print(type(e))

print("step 4")