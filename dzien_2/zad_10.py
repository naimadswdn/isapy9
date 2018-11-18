# This program is going to check if provided year is a leap-year or not

print('Hello! This program is going to check if provided year is a leap-year or not')

year = input('Please provide a year: ')
year = int(year)

if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year} is a leap-year.')
else:
    print(f'{year} is NOT a leap-year.')
