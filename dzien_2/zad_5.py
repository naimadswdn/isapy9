# This program is going to draw a rectangle based on provided dimensions


def rectangle():
    """This program is going to draw a rectangle based on provided dimensions."""
    import time
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good
    print("Hello! This program is going to draw a rectangle based on provided dimensions.")
    time.sleep(2)

    while True:
        width = None
        width = check_if_good(width, int, 'Please provide width of rectangle: ')
        if width == 0:
            print('Width cannot be 0! Please correct it!')
            continue
        else:
            break

    while True:
        length = None
        length = check_if_good(length, int, 'Please provide length of rectangle: ')
        if length == 0:
            print('Length cannot be 0! Please correct it!')
            continue
        else:
            break

    elements = ['|', '-', '+', ' ']

    print(elements[2], (width - 2) * elements[1], elements[2])
    for i in range(length - 2):
        print(elements[0], (width - 2) * elements[3], elements[0])
    print(elements[2], (width - 2) * elements[1], elements[2])

    repeat_y_or_n(rectangle, "Would you like to draw another rectangle?")


def main():
    rectangle()


if __name__ == "__main__":
    main()
