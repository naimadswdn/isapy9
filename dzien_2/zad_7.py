# Program to check if provided number is even or not.

def if_even():
    while True:
        number = input('Please provide number: ')
        if int(number) % 2 == 0:
            print('Your number is even!')
            user_choise = input('Would you like to check another number? Type "y" if yes, or "n" if no. ')
            if user_choise == 'y':
                continue
            else:
                break
        else:
            print('Your number is odd!')
            user_choise = input('Would you like to check another number? Type "y" if yes, or "n" if no. ')
            if user_choise == 'y':
                continue
            else:
                break


if_even()