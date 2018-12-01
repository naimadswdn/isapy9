
def if_even():
    """Program to check if provided number is even or not."""
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good
    from time import sleep

    print('Hello! This program is going to check if provided number is even or not.')
    sleep(1.5)
    number = None
    number = check_if_good(number, float, 'Please provide number: ')
    if float(number) % 2 == 0:
        print('Your number is even!')
        repeat_y_or_n(if_even)

    else:
        print('Your number is odd!')
        repeat_y_or_n(if_even)


def main():
    if_even()


if __name__ == "__main__":
    main()
