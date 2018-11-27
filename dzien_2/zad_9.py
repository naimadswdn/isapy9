

def devided_by_and_3_5_7():
    """Program to check if number is divided by 3 and 5 and 7 at the same time."""
    print('Hello! This program is going to check if provided number is divided by 3 and 5 and 7.')

    number = input('Please provide number: ')
    number = int(number)
    result = 0

    for i in (3, 5, 7):
        if number % i == 0:
            result += 1

    if result == 3:
        print(f'{number} is divided by 3 and 5 and 7 at the same time!')
    else:
        print(f'{number} is NOT divided by 3 and 5 and 7 at the same time :(.')


devided_by_and_3_5_7()
