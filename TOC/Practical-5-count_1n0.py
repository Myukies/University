def count_ones_and_zeros(string):
    ones = string.count('1')
    zeros = string.count('0')
    return ones, zeros

# Example usage
input_string = input("Enter a string: ")
ones, zeros = count_ones_and_zeros(input_string)
print(f"Number of 1's: {ones}, Number of 0's: {zeros}")
