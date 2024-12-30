from collections.abc import Iterable, Iterator

class MyList(object):
    def __init__(self):
        self.data = []
        self.index = 0

    def add_item(self, item):
        self.data.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            self.index = 0
            raise StopIteration()
        else:
            self.index += 1
            return self.data[self.index - 1]
        
if __name__ == '__main__':
    mylist = MyList()
    mylist.add_item("Stringdd")
    mylist.add_item(123)
    mylist.add_item(3.14)
    mylist.add_item([1, 2, 3])
    
    print('mylist is iterable?', isinstance(mylist, Iterable))
    print('mylist is iterator?', isinstance(mylist, Iterator))
    

    print(list(mylist))