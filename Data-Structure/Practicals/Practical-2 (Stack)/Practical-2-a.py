class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack size:", stack.size())
print("Top element:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Is the stack empty?", stack.is_empty())
