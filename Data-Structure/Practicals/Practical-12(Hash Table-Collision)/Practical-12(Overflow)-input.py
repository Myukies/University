class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def traverse(self):
        for index in range(self.size):
            current = self.table[index]
            while current is not None:
                print(f"Key: {current.key}, Value: {current.value}")
                current = current.next

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next


if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\nMenu:")
        print("1. Insert Key-Value Pair")
        print("2. Delete Key")
        print("3. Get Value by Key")
        print("4. Traverse Hash Table")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the key: "))
            value = input("Enter the value: ")
            hash_table.insert(key, value)
        elif choice == 2:
            key = int(input("Enter the key to delete: "))
            hash_table.delete(key)
        elif choice == 3:
            key = int(input("Enter the key to get the value: "))
            value = hash_table.get(key)
            if value is not None:
                print(f"Value for key {key}: {value}")
            else:
                print(f"Key {key} not found in the hash table.")
        elif choice == 4:
            print("Hash Table:")
            hash_table.traverse()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
