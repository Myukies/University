class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def in_queue(self, data):
        self.queue.append(data)

    def de_queue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:")
            for item in self.queue:
                print(item, end=" <- ")
            print("Front")

if __name__ == "__main__":
    queue = Queue()

    print("Queue Operations:")
    while True:
        print("\n1. Enqueue (Insert an element)")
        print("2. Dequeue (Remove an element)")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            data = input("Enter the element to enqueue: ")
            queue.in_queue(data)
            print(f"{data} enqueued to the Queue.")

        elif choice == 2:
            de_queued_element = queue.de_queue()
            if de_queued_element is not None:
                print(f"Dequeued element: {de_queued_element}")
            else:
                print("Queue is empty. Cannot dequeue.")

        elif choice == 3:
            queue.display()

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

