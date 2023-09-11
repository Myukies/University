class Node:
    def init (self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def init (self, size):
        self.size = size
        self.table = [None] * size

    def hash_function (self, key):
        return key % self.size

    def insert (self, key, value):
        index = self.hash_function (key)
        if self.table [index] is None:
            self.table [index] = Node (key, value)
        else:
            current = self.table [index]
        while current.next is not None:
            current = current.next
        current.next = Node (key, value)
    def delete (self, key) :
        index = self.hash_function (key)
        if self.table [index] is not None:
                if self.table [index].key == key:
                    self.table [index] = self.table [index].next
                else:
                    current = self.table [index]
                    while current.next is not None: 
                        if current.next.key == key:
                            current.next = current.next.next
                            return
                current = current.next