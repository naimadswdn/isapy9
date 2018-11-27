

def binary_to_digit():
    """Program to convert 6 digit binary number to decimal number"""
    import time

    print('Hello! This program is going to convert 6 digit binary number to decimal number.')
    time.sleep(2)

    while True:
        binary = input('Please provide binary number with exactly 6 digits and using only 0/1 numbers: ')
        if len(binary) != 6:
            print('Your number is not 6 digits! Please correct it. ')
            continue
        else:
            break

    values = [1, 2, 4, 8, 16, 32]

    decimal = int(binary[-1]) * values[0] + int(binary[-2]) * values[1] + int(binary[-3]) * values[2] + int(binary[-4]) * values[3] + int(
            binary[-5]) * values[4] + int(binary[-6]) * values[5]

    print(f'Binary {binary} is equal to {decimal} in decimal system.')


binary_to_digit()


