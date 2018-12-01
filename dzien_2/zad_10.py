
def is_leap_year():
    """This program is going to check if provided year is a leap-year or not."""
    from time import sleep
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello! This program is going to check if provided year is a leap-year or not.')
    sleep(1.5)

    year = None
    year = check_if_good(year, int, 'Please provide a year: ')
    year = int(year)

    if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year} is a leap-year.')
    else:
        print(f'{year} is NOT a leap-year.')

    repeat_y_or_n(is_leap_year)


def main():
    is_leap_year()


if __name__ == "__main__":
    main()
