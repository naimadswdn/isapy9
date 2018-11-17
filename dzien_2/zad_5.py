# This program is going to draw a rectangle based on provided dimensions
import time

print('Hello! This program is going to draw a rectangle based on provided dimensions.')

time.sleep(2)

width = input('Please provide width of rectangle: ')
width = int(width)
length = input('Please provide length of rectangle: ')
length = int(length)

side = '|'
base = '-'
apex = '+'
space = ' '


def rectangle():
    print(apex, (width - 2) * base, apex)
    for i in range(length - 2):
        print(side, (width - 2) * space, side)
    print(apex, (width - 2) * base, apex)


rectangle()
