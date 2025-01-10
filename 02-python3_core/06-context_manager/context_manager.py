from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    yield f
    f.close()

with open_file('data/sample.txt', 'w') as f:
    f.write('Hello, World!\n')