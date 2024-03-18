def is_divisible_by_2(number):
    return int(number * 10) % 2 == 0

def main():
    decimal_number = float(input("Enter a decimal number: "))
    if is_divisible_by_2(decimal_number):
        print("The number", decimal_number, "is divisible by 2.")
    else:
        print("The number", decimal_number, "is not divisible by 2.")

if __name__ == "__main__":
    main()
