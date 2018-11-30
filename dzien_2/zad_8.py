
def divided_by_or_3_5_7():
    """Program to check if number is divided by 3 or 5 or 7"""
    from time import sleep
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello! This program is going to check if provided number is divided by 3 or 5 or 7.')
    sleep(1.5)

    number = None
    number = check_if_good(number, int, 'Please provide number: ')
    number = int(number)

    for i in (3, 5, 7):
        if number % i == 0:
            print(f'{number} is divided by {i}.')
        else:
            print(f'{number} is not divided by {i}.')
    sleep(1)
    repeat_y_or_n(divided_by_or_3_5_7)


divided_by_or_3_5_7()
