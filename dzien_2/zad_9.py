

def divided_by_and_3_5_7():
    """Program to check if number is divided by 3 and 5 and 7 at the same time."""
    from time import sleep
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello! This program is going to check if provided number is divided by 3 and 5 and 7.')
    sleep(1.5)

    number = None
    number = check_if_good(number, int, 'Please provide number: ')
    number = int(number)
    result = 0

    for i in (3, 5, 7):
        if number % i == 0:
            result += 1

    if result == 3:
        print(f'{number} is divided by 3 and 5 and 7 at the same time!')
    else:
        print(f'{number} is NOT divided by 3 and 5 and 7 at the same time :(.')

    sleep(1)
    repeat_y_or_n(divided_by_and_3_5_7)


def main():
    divided_by_and_3_5_7()


if __name__ == "__main__":
    main()
