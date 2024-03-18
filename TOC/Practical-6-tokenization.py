import re

def tokenize(input_string):
    tokens = re.findall(r'\w+|[^\w\s]', input_string)
    return tokens

# Example usage
input_string = input("Enter a string: ")
print("Tokens:", tokenize(input_string))
