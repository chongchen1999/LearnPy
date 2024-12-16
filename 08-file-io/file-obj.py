with open("data/example.txt", "r") as f:
    print("File name: {0}".format(str(f.name)))
    print(f.tell())
    print("Contents that read:\n{0}\n".format(f.readline()))
    print(f.tell())
    f.seek(0, 0)
    print("Contents that read:\n{0}\n".format(f.readline()))