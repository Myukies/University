def create_2d_array(rows, cols):
    array = []
    print(f"Enter the elements of the {rows}x{cols} array:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i}, {j}): "))
            row.append(element)
        array.append(row)
    return array

def print_2d_array(array):
    for row in array:
        print(' '.join(str(element) for element in row))

def add_arrays(array1, array2):
    rows = len(array1)
    cols = len(array1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = array1[i][j] + array2[i][j]
            row.append(element)
        result.append(row)
    return result

def subtract_arrays(array1, array2):
    rows = len(array1)
    cols = len(array1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = array1[i][j] - array2[i][j]
            row.append(element)
        result.append(row)
    return result

def multiply_arrays(array1, array2):
    rows1 = len(array1)
    cols1 = len(array1[0])
    cols2 = len(array2[0])
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += array1[i][k] * array2[k][j]
            row.append(element)
        result.append(row)
    return result

def transpose_array(array):
    rows = len(array)
    cols = len(array[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            element = array[i][j]
            row.append(element)
        result.append(row)
    return result


# Example usage
rows1 = int(input("Enter the number of rows for array 1: "))
cols1 = int(input("Enter the number of columns for array 1: "))
array1 = create_2d_array(rows1, cols1)

rows2 = int(input("Enter the number of rows for array 2: "))
cols2 = int(input("Enter the number of columns for array 2: "))
array2 = create_2d_array(rows2, cols2)

print("Array 1:")
print_2d_array(array1)

print("Array 2:")
print_2d_array(array2)

# Addition
if rows1 == rows2 and cols1 == cols2:
    addition_result = add_arrays(array1, array2)
    print("Addition Result:")
    print_2d_array(addition_result)
else:
    print("Array dimensions do not match for addition.")

# Subtraction
if rows1 == rows2 and cols1 == cols2:
    subtraction_result = subtract_arrays(array1, array2)
    print("Subtraction Result:")
    print_2d_array(subtraction_result)
else:
    print("Array dimensions do not match for subtraction.")

# Multiplication
if cols1 == rows2:
    multiplication_result = multiply_arrays(array1, array2)
    print("Multiplication Result:")
    print_2d_array(multiplication_result)
else:
    print("Array dimensions do not match for multiplication.")

# Transpose
transpose_result = transpose_array(array1)
print("Transpose Result:")
print_2d_array(transpose_result)

