class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print("exiting...")
        self.file.close()


with File('data/test.txt', 'w') as f:
    print("writing...")
    f.write('Testing context manager')