# Simple script to show first and last digit of provided number


def first_last():
    """Simple script to show first and last digit of provided number"""
    import time
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print("Hello! This program is going to show first and last digit of provided number.")
    time.sleep(3)

    number = None
    number = check_if_good(number, str, "Please provide a number: ")
    first_digit = number[0]
    last_digit = number[-1:]
    print(f'Your number is {number}.')
    print(f'First digit of yoy number is {first_digit}.')
    print(f'Last digit of you number is {last_digit}.')

    repeat_y_or_n(first_last, 'Would you like to work with another number?')

#
# def next_number():
#     print('Would you like to work with another number?')
#     while True:
#         user_choise = input('Please type "y" if yes, or "n" if no.')
#         if user_choise == 'y':
#             first_last()
#             print('Would you like to work with another number?')
#             continue
#         elif user_choise == 'n':
#             break
#         else:
#             print('Wrong answer. Please type "y" or "n".')
#             continue


first_last()

