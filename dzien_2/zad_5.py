# This program is going to draw a rectangle based on provided dimensions


def rectangle():
    """Hello! This program is going to draw a rectangle based on provided dimensions."""
    import time

    time.sleep(2)

    while True:
        width = input('Please provide width of rectangle: ')
        width = int(width)
        if width == 0:
            print('Width cannot be 0! Please correct it!')
            continue
        else:
            break

    while True:
        length = input('Please provide length of rectangle: ')
        length = int(length)
        if length == 0:
            print('Length cannot be 0! Please correct it!')
            continue
        else:
            break

    side = '|'
    base = '-'
    apex = '+'
    space = ' '

    print(apex, (width - 2) * base, apex)
    for i in range(length - 2):
        print(side, (width - 2) * space, side)
    print(apex, (width - 2) * base, apex)


rectangle()
