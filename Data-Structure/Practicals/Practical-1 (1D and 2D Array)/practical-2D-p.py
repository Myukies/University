class Array2D:
    def __init__(self):
        self.array = []

    def add_row(self, row_data):
        self.array.append(row_data)

    def delete_element(self, row_index, col_index):
        if 0 <= row_index < len(self.array) and 0 <= col_index < len(self.array[row_index]):
            self.array[row_index].pop(col_index)
            print("Element deleted successfully.")
        else:
            print("Invalid indices. Please provide valid row and column indices.")

    def search_element(self, element):
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j] == element:
                    return i, j
        return None

    def sort_array(self):
        self.array.sort()

    def merge_arrays(self, other_array):
        if isinstance(other_array, Array2D):
            self.array.extend(other_array.array)
            print("Arrays merged successfully.")
        else:
            print("Invalid input. Cannot merge with a non-2D array.")

    def display_array(self):
        if not self.array:
            print("Array is empty.")
        else:
            print("Array elements:")
            for row in self.array:
                print(" ".join(str(element) for element in row))

if __name__ == "__main__":
    print("2D Array Operations")

    arr = Array2D()

    while True:
        print("\nOptions:")
        print("1. Add row to the array")
        print("2. Delete element from the array")
        print("3. Search for an element in the array")
        print("4. Sort the array")
        print("5. Merge with another array")
        print("6. Display the array")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            row_data = input("Enter elements of the row separated by spaces: ").split()
            row_data = [int(element) for element in row_data]
            arr.add_row(row_data)
        elif choice == 2:
            row_index = int(input("Enter the row index: "))
            col_index = int(input("Enter the column index: "))
            arr.delete_element(row_index, col_index)
        elif choice == 3:
            element = int(input("Enter the element to search: "))
            result = arr.search_element(element)
            if result:
                row, col = result
                print(f"Element found at row {row}, column {col}.")
            else:
                print("Element not found.")
        elif choice == 4:
            arr.sort_array()
        elif choice == 5:
            arr2 = Array2D()
            print("Enter the second array:")

            while True:
                row_data = input("Enter elements of the row separated by spaces (or type 'done' to stop): ")
                if row_data.lower() == 'done':
                    break
                row_data = row_data.split()
                row_data = [int(element) for element in row_data]
                arr2.add_row(row_data)

            arr.merge_arrays(arr2)
        elif choice == 6:
            arr.display_array()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
