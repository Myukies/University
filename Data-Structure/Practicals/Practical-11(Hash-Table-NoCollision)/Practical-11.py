class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def display(self):
        for entry in self.table:
            if entry:
                print(f'Key: {entry[0]}, Value: {entry[1]}')

hash_table = HashTable(10)

while True:
    print("\nOptions:")
    print("1. Insert")
    print("2. Delete")
    print("3. Get")
    print("4. Display/Traverse")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        k = int(input("Enter Key to insert: "))
        v = input("Enter Value to insert: ")
        hash_table.insert(k, v)
    elif choice == 2:
        k = int(input("Enter Key to Delete: "))
        hash_table.delete(k)
    elif choice == 3:
        k = int(input("Enter Key to Get: "))
        result = hash_table.get(k)
        if result is not None:
            print(f'Value: {result}')
        else:
            print("Key not found.")
    elif choice == 4:
        print("Hash Table:")
        hash_table.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please select a valid option.")