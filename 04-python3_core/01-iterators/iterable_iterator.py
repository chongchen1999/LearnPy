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
    for i in range(5):
        mylist.add_item(i)
    
    print('mylist is iterable?', hasattr(mylist, '__iter__'))
    print('mylist is iterator?', hasattr(mylist, 'next'))
    
    for x in mylist:
        print(x)