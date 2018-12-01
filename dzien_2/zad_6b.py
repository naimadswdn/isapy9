
def binary_to_decimal_int():
    """Program to convert any binary number to it's decimal equivalent."""
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    while True:
        try:
            binary = input('Please provide binary number: ')
            decimal = int(binary, 2)
            print(f'Your binary {binary} number is equal to decimal {decimal}.')
            break
        except:
            print('Wrong binary number! Please correct it by using only 0 or 1.')
            continue
    repeat_y_or_n(binary_to_decimal_int)


def main():
    binary_to_decimal_int()


if __name__ == "__main__":
    main()
