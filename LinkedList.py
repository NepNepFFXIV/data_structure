class Node:
    __slots__ = ['data', 'next']
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node(data = {self.data}, next = {self.next.data if self.next is not None else None})'

class LinkedList:
    __slots__ = ['head', 'tail', 'size']
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        new_node = Node(item)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:                       # Empty list
            raise IndexError("List is empty")
        if self.head is self.tail:                  # Only 1 element in the list
            self.tail = None
        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        if self.head is None:                       # Empty list
            raise IndexError("List is empty")
        if self.head is self.tail:                  # Only 1 element in the list
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        self.size -= 1

    def __getitem__(self, key):
        if self.head is None:
            raise IndexError("List is empty")

        if isinstance(key, slice):  # Assuming step is always 1
            if key.start is None:
                start = 0
            else:
                start = self.size + key.start if key.start < 0 else key.start

            if key.stop is None:
                stop = self.size
            else:
                stop = self.size + key.stop if key.stop < 0 else key.stop
            stop = min(stop, self.size)

            if start >= stop:
                return []

            result = []
            current_index = 0
            current_node = self.head
            while current_index < stop:
                if current_index >= start:
                    result.append(current_node.data)                
                current_index += 1
                current_node = current_node.next
            return result        
        elif isinstance(key, int):
            if not (-self.size <= key < self.size):
                raise IndexError("list index out of range")

            current_node = self.head
            current_index = 0
            key = self.size + key if key < 0 else key
            while current_index != key:
                current_index += 1
                current_node = current_node.next            
            return current_node.data
        else:
            raise TypeError("Key type not supported")

    def __setitem__(self, key, item):
        if self.head is None:
            raise IndexError("List is empty")
        
        if isinstance(key, slice):  # Assuming step is always 1
            if key.start is None:
                start = 0
            else:
                start = self.size + key.start if key.start < 0 else key.start
            start = min(start, self.size)
            start = 0 if start < 0 else start

            if key.stop is None:
                stop = self.size
            else:
                stop = self.size + key.stop if key.stop < 0 else key.stop
            stop = min(stop, self.size)
            stop = start if stop < start else stop

            new_first_node = Node(item[0])
            new_last_node = new_first_node
            for i in item[1:]:
                new_node = Node(i)
                new_last_node.next = new_node
                new_last_node = new_node

            prev_node = None
            current_node = self.head
            current_index = 0
            while current_index != start:
                prev_node = current_node
                current_node = current_node.next
                current_index += 1

            # Setting head if neccessary
            if prev_node is None:
                self.head = new_first_node
            else:
                prev_node.next = new_first_node           

            # Setting tail if neccessary
            if current_index == self.size:
                self.tail = new_last_node
            else:
                while current_index != stop:
                    current_node = current_node.next
                    current_index += 1
                new_last_node.next = current_node
            self.size = self.size - (stop - start) + len(item)
        elif isinstance(key, int):
            if not (-self.size <= key < self.size):
                raise IndexError("list assignment index out of range")

            current_node = self.head
            current_index = 0
            key = self.size + key if key < 0 else key
            while current_index != key:
                current_index += 1
                current_node = current_node.next            
            current_node.data = item
        else:
            raise TypeError("Key type not supported")

    def __delitem__(self, key):
        if self.head is None:
            raise IndexError("List is empty")

        if isinstance(key, slice):  # Assuming step is always 1
            if key.start is None:
                start = 0
            else:
                start = self.size + key.start if key.start < 0 else key.start
            start = min(start, self.size)
            start = 0 if start < 0 else start

            if key.stop is None:
                stop = self.size
            else:
                stop = self.size + key.stop if key.stop < 0 else key.stop
            stop = min(stop, self.size)
            stop = start if stop < start else stop

            if start == 0:
                for _ in range(stop):
                    self.remove_first()
            else:                           
                prev_node = None
                current_node = self.head
                current_index = 0
                while current_index != start:
                    current_index += 1
                    prev_node = current_node
                    current_node = current_node.next
                if stop == self.size:       # head node is guaranteed not deleted
                    prev_node.next = None
                    self.tail = prev_node
                else:                       # delete nodes between head and tail
                    last_node = current_node
                    while current_index != stop:
                        current_index += 1
                        last_node = last_node.next
                    prev_node.next = last_node
                self.size -= (stop - start)
        elif isinstance(key, int):
            if not (-self.size <= key < self.size):
                raise IndexError("list index out of range")
            key = self.size + key if key < 0 else key

            if key == 0:
                self.remove_first()
            elif key == self.size-1:
                self.remove_last()
            else:
                prev_node = None
                current_node = self.head
                current_index = 0
                while current_index < key:
                    current_index += 1
                    prev_node = current_node
                    current_node = current_node.next
                prev_node.next = current_node.next
                current_node = None
                self.size -= 1
        else:
            raise TypeError("Key type not supported")

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def __repr__(self):
        if self.head is None:
            return "[]"

        current_node = self.head
        result = f'[{repr(current_node.data)}'
        while current_node.next is not None:
            current_node = current_node.next
            result += f', {repr(current_node.data)}'

        return result + ']'

    def __str__(self):
        return repr(self)
