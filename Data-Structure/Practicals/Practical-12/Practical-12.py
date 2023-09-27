
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")

if __name__ == "__main__":
    table = HashTable(10)

    table.insert("Siddhant", 21)
    table.insert("Pratyush", 21)
    table.insert("Atharva", 20)
    table.insert("Ameen", 20)

    print("Displaying the hash table:")
    table.display()

    print("\nSearching for 'Siddhant'...", table.search("Siddhant"))
    print("Searching for 'Atharva'...", table.search("Atharva"))

    print("\nDeleting 'Ameen'...")
    table.delete("Ameen")
    table.display()
