while True:
    try:
        x = int(input("Input a number: "))
        print("The number is", x)
        if x == 88:
            print("Exiting...")
            break
    except ValueError as e:
        print("Invalid input. Please enter an integer.")
        print(ValueError)
        print(e)


print("Done")