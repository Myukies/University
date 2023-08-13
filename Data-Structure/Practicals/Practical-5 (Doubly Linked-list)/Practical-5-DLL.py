class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_first(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def add_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                break
            current = current.next


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    print("Welcome to the Doubly Linked List!")
    while True:
        print("\n1. Display List (Forward)")
        print("2. Display List (Backward)")
        print("3. Check if Empty")
        print("4. Add to First")
        print("5. Remove from First")
        print("6. Add to Tail")
        print("7. Remove from Tail")
        print("8. Insert After Element")
        print("9. Exit")

        choice = int(input("Enter your choice (1-9): "))

        if choice == 1:
            print("Doubly Linked List (Forward):")
            linked_list.display_forward()

        elif choice == 2:
            print("Doubly Linked List (Backward):")
            linked_list.display_backward()

        elif choice == 3:
            if linked_list.is_empty():
                print("The doubly linked list is empty.")
            else:
                print("The doubly linked list is not empty.")

        elif choice == 4:
            data = int(input("Enter the data to add at the beginning: "))
            linked_list.add_first(data)
            print(f"{data} added to the beginning of the doubly linked list.")

        elif choice == 5:
            linked_list.remove_first()
            print("Removed the first element from the doubly linked list.")

        elif choice == 6:
            data = int(input("Enter the data to add at the end: "))
            linked_list.add_tail(data)
            print(f"{data} added to the end of the doubly linked list.")

        elif choice == 7:
            linked_list.remove_tail()
            print("Removed the last element from the doubly linked list.")

        elif choice == 8:
            target_data = int(input("Enter the data after which to insert: "))
            data = int(input("Enter the data to insert: "))
            linked_list.insert_after(target_data, data)
            print(f"{data} inserted after {target_data} in the doubly linked list.")

        elif choice == 9:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

