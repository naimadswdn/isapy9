# Program to convert 6 digit binary number to decimal number

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


first = 1
second = 2
third = 4
fourth = 8
fifth = 16
sixth = 32

decimal = int(binary[-1]) * first + int(binary[-2]) * second + int(binary[-3]) * third + int(binary[-4]) * fourth + int(
        binary[-5]) * fifth + int(binary[-6]) * sixth

print(f'Binary {binary} is equal to {decimal} in decimal system.')



