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

    def print_is_empty(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")


stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        item = input("Enter the item to push: ")
        stack.push(item)
        print("Item pushed onto the stack.")
    elif choice == "2":
        try:
            item = stack.pop()
            print("Popped item:", item)
        except IndexError as e:
            print("Error:", str(e))
    elif choice == "3":
        try:
            item = stack.peek()
            print("Top element:", item)
        except IndexError as e:
            print("Error:", str(e))
    elif choice == "4":
        print("Stack size:", stack.size())
    elif choice == "5":
        stack.print_is_empty()
    elif choice == "6":
        print("Quitting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
