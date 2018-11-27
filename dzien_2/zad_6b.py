
def binary_to_decimal_int():
    """Program to convert any binary number to it's decimal equivalent."""

    while True:
        try:
            binary = input('Please provide binary number: ')
            decimal = int(binary, 2)
            print(f'Your binary {binary} number is equal to decimal {decimal}.')
            break
        except:
            print('Wrong binary number! Please correct it by using only 0 or 1.')
            continue


binary_to_decimal_int()