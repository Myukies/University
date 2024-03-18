def equal_ones_and_zeros(string):
    state = 0
    for char in string:
        if char == '1':
            state += 1
        elif char == '0':
            state -= 1
        else:
            return False  # Reject if there are characters other than 0 or 1
        if state < 0:
            return False  # Reject if the count of 0's exceeds the count of 1's
    return state == 0  # Accept if the count of 1's equals the count of 0's

# Example usage
input_string = input("Enter a string: ")
if equal_ones_and_zeros(input_string):
    print("String accepted")
else:
    print("String not accepted")
