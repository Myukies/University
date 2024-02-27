class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1]) 

    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]
        else:
            print("Priority Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def traverse(self):
        if not self.is_empty():
            for item, priority in self.queue:
                print(f"Item: {item}, Priority: {priority}")
        else:
            print("Priority Queue is empty.")



if __name__ == "__main__":
    pq = PriorityQueue()
    

    pq.insert('Task 1', 3)
    pq.insert('Task 2', 1)
    pq.insert('Task 3', 2)
    pq.insert('Task 4', 4)
 
    print("Priority Queue Contents:")
    pq.traverse()

    print("\nDeletion:")
    print("Deleted item:", pq.delete())
    print("Deleted item:", pq.delete())
    print("Deleted item:", pq.delete())
    print("Deleted item:", pq.delete())
    print("Deleted item:", pq.delete())  
