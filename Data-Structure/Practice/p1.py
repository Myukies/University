class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            print("Empty Stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            print("Empty Stack")
        return self.items[-1]

    def print_stack(self):
        print("Stack contents:")
        for item in reversed(self.items):
            print(item)
    

stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

print("\n Is Empty? ", stack.is_empty())
print("\n Stack Size: ", stack.size())
print("\n Top Element: ", stack.peek())
stack.print_stack()

pop_item = stack.pop()
print("Popped item: ", pop_item)
pop_item = stack.pop()
print("Popped item: ", pop_item)


print("\n Is Empty? ", stack.is_empty())
print("\n Stack Size: ", stack.size())
print("\n Top Element: ", stack.peek())
stack.print_stack()
