with open("data/example.txt", "r") as f:
    lines = f.readlines()
    lines = ["#" + str(index) + " " + line for index, line in enumerate(lines)]

print(lines)
with open("data/example_numbered.txt", "w") as f:
    f.writelines(lines)