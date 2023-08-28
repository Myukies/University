class Array:
    def __init__(self):
        self.array = []

    def add_element(self, element):
        self.array.append(element)

    def delete_element(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
            print("Element deleted successfully.")
        else:
            print("Index out of range. Please provide a valid index.")

    def search_element(self, element):
        for i in range(len(self.array)):
            if self.array[i] == element:
                return i
        return -1

    def sort_array(self):
        self.array.sort()
        print("Array sorted successfully.")

    def merge_arrays(self, other_array):
        if isinstance(other_array, Array):
            self.array.extend(other_array.array)
            print("Arrays successfully merged.")
        else:
            print("Invalid input. Cannot merge with a non-1D array.")

    def display_array(self):
        if not self.array:
            print("Array is empty.")
        else:
            print("Array elements:")
            for element in self.array:
                print(element, end=" ")
            print()


if __name__ == "__main__":
    print("1D Array Operations")

    arr = Array()

    while True:
        print("\nOptions:")
        print("1. Add element to the array")
        print("2. Delete element from the array")
        print("3. Search for an element in the array")
        print("4. Sort the array")
        print("5. Merge with another array")
        print("6. Display the array")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            elements = input("Enter elements separated by spaces: ").split()
            elements = [int(element) for element in elements]
            for element in elements:
                arr.add_element(element)
        elif choice == 2:
            index = int(input("Enter the index to delete: "))
            arr.delete_element(index)
        elif choice == 3:
            element = int(input("Enter the element to search: "))
            index = arr.search_element(element)
            if index != -1:
                print(f"Element found at index {index}.")
            else:
                print("Element not found.")
        elif choice == 4:
            arr.sort_array()
        elif choice == 5:
            arr2 = Array()
            elements = input("Enter elements of the second array separated by spaces: ").split()
            elements = [int(element) for element in elements]
            for element in elements:
                arr2.add_element(element)
            arr.merge_arrays(arr2)
        elif choice == 6:
            arr.display_array()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
