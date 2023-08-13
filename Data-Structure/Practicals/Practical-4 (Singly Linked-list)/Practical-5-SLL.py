class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def add_first(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def remove_first(self):
        if self.head:
            self.head = self.head.next_node

    def add_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def remove_tail(self):
        if not self.head:
            return

        if not self.head.next_node:
            self.head = None
            return

        previous_node = None
        current_node = self.head
        while current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
        previous_node.next_node = None

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                break
            current_node = current_node.next_node


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    print("Welcome to the Singly Linked List!")
    while True:
        print("\n1. Display List")
        print("2. Check if Empty")
        print("3. Add to First")
        print("4. Remove from First")
        print("5. Add to Tail")
        print("6. Remove from Tail")
        print("7. Insert After Element")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            print("Linked List:")
            linked_list.display()

        elif choice == 2:
            if linked_list.is_empty():
                print("The linked list is empty.")
            else:
                print("The linked list is not empty.")

        elif choice == 3:
            data = int(input("Enter the data to add at the beginning: "))
            linked_list.add_first(data)
            print(f"{data} added to the beginning of the linked list.")

        elif choice == 4:
            linked_list.remove_first()
            print("Removed the first element from the linked list.")

        elif choice == 5:
            data = int(input("Enter the data to add at the end: "))
            linked_list.add_tail(data)
            print(f"{data} added to the end of the linked list.")

        elif choice == 6:
            linked_list.remove_tail()
            print("Removed the last element from the linked list.")

        elif choice == 7:
            target_data = int(input("Enter the data after which to insert: "))
            data = int(input("Enter the data to insert: "))
            linked_list.insert_after(target_data, data)
            print(f"{data} inserted after {target_data} in the linked list.")

        elif choice == 8:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

