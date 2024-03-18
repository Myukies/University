def accepts_101(string):
    if string.endswith('101'):
        return True
    return False

# Example usage
input_string = input("Enter a string: ")
if accepts_101(input_string):
    print("String accepted")
else:
    print("String not accepted")
