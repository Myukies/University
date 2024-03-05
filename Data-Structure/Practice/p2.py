class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    def push(self):
        self.items.append()
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack Empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    
