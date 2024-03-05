class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key = lambda x : x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("Empty")
    
    def size(self):
        return len(self.items)