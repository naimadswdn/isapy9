# Program to check if number is divided by 3 or 5 or 7

print('Hello! This program is going to check if provided number is divided by 3 or 5 or 7.')

number = input('Please provide number: ')
number = int(number)

for i in (3, 5, 7):
    if number % i == 0:
        print(f'{number} is divided by {i}.')
    else:
        print(f'{number} is not divided by {i}.')
