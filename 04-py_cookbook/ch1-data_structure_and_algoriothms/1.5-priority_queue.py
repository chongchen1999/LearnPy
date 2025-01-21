import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []  # The heap (list) to store the items
        self._index = 0   # A counter to keep track of insertion order

    def push(self, item, priority):
        # Push a tuple of (-priority, index, item) onto the heap
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1  # Increment the index for the next item

    def pop(self):
        # Pop the smallest item from the heap (which is the highest priority)
        return heapq.heappop(self._queue)[-1]  # Return the item (last element of the tuple)
    
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name!r})'

# Create a priority queue
q = PriorityQueue()

# Push items with priorities
q.push(Item('foo'), 1)  # Priority 1
q.push(Item('bar'), 5)  # Priority 5
q.push(Item('spam'), 4) # Priority 4
q.push(Item('grok'), 1) # Priority 1

# Pop items
print(q.pop())  # Output: Item('bar')  (highest priority)
print(q.pop())  # Output: Item('spam') (next highest priority)
print(q.pop())  # Output: Item('foo')  (same priority as 'grok', but inserted first)
print(q.pop())  # Output: Item('grok') (same priority as 'foo', but inserted second)