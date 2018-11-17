# Simple script to calculate surface area of circle, based on provided radius
import math

print("Hello! This program is going to calculate surface area of circle, based on provided radius. ")

radius = input("Please provide value of circle radius [cm]: ")
radius = int(radius)
pattern = round(math.pi,5) * (radius ** 2)
print(f'Following pattern is going to be used to calculate surface area: pi*(radius**2)')


def choice():
    print('Please write "y" if you would like to see calculations step by step. Write "n" if you want only result')
    while True:
        user_choice = input()
        if user_choice == 'y':
            print(f'Step one: substitution of your value to the pattern: \nP=pi*({radius}**2)')
            print(f'Step two: calculating results..\nPi constant is estimated to {round(math.pi,5)}.')
            print(f'Result: Surface area of circle with radius {radius} cm is equal to {round(pattern,2)} cm\u00b2.')
            break
        elif user_choice == 'n':
            print(f'Result: Surface area of circle with radius {radius} cm is equal to {round(pattern,2)} cm\u00b2.')
            break
        else:
            print('Wrong answer! Please write "y" or "n".')
            continue


choice()
