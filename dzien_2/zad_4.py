# Simple script to show first and last digit of provided number


def first_last():
    """Hello! This program is going to show first and last digit of provided number."""
    import time

    time.sleep(3)

    number = input("Please provide number: ")
    first_digit = number[0]
    last_digit = number[-1:]
    print(f'Your number is {number}.')
    print(f'First digit of yoy number is {first_digit}.')
    print(f'Last digit of you number is {last_digit}.')


def next_number():
    print('Would you like to work with another number?')
    while True:
        user_choise = input('Please type "y" if yes, or "n" if no.')
        if user_choise == 'y':
            first_last()
            print('Would you like to work with another number?')
            continue
        elif user_choise == 'n':
            break
        else:
            print('Wrong answer. Please type "y" or "n".')
            continue


first_last()
next_number()
