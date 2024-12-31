from collections.abc import Iterable, Iterator

class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        # print('MyList.__iter__ called')
        return MyListIterator(self.container)

class MyListIterator(object):
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        # print('MyListIterator.__next__ called')
        if self.index < len(self.container):
            item = self.container[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self

my_list = MyList()
for i in range(10):
    my_list.add(i)

my_list_iter : MyListIterator = iter(my_list)

print(isinstance(my_list, Iterable)) 
print(isinstance(my_list_iter, Iterable))
print(isinstance(my_list_iter, Iterator))

for item in my_list:
    print(item, end=' ')