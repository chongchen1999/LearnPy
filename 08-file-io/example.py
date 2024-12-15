with open("data/example.txt", "a") as f:
    f.write("This is a test!\n")

with open("data/example.txt", "r") as f:
    for s in f.readlines():
        print(s, end = "")