def accepts_three_consecutive_ones(string):
    if '111' in string and '1111' not in string:
        return True
    return False

# Example usage
input_string = input("Enter a string: ")
if accepts_three_consecutive_ones(input_string):
    print("String accepted")
else:
    print("String not accepted")
