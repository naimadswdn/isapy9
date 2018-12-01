# Interface for all created programs - it allows to choose program from the menu


def print_programs_list():
    """Program to print list of all available programs."""
    from time import sleep

    print("Hello in Multitool Python by Damian.\nFull list of available programs:: ")
    sleep(1.5)

    programs = ['Celsius to Fahrenheit converter.',
                'Fahrenheit to Celsius converter.',
                'Calculator of surface area of circle.',
                'First and last digit of provided number.',
                'Draw a rectangle.',
                'Binary to decimal converter.',
                'Check if number is even or odd.',
                'Check if number is divided by 3 or 5 or 7',
                'Check if provided number is divided by 3 and 5 and 7',
                'Check if provided year is a leap-year.',
                'Print list elements in fancy table.',
                'Calculator of remainder from cash.',
                'Draw a pyramid',
                'Calculator od your dog age in dog\'s scale'
                ]

    for i, program_name in enumerate(programs, start=1):
        print(f' {i}. {program_name}')
        #last_number = i



def multitool():
    """Interface for all created programs that allow user to choose interesting one."""
    from dzien_2.check_if_good import check_if_good
    from dzien_2.zad_1 import celsius_to_fahrenheit
    from dzien_2.zad_2 import fahrenheit_to_celsius
    from dzien_2.zad_3 import surface_area_of_circle
    from dzien_2.zad_4 import first_last
    from dzien_2.zad_5 import rectangle
    from dzien_2.zad_6b import binary_to_decimal_int
    from dzien_2.zad_7 import if_even
    from dzien_2.zad_8 import divided_by_or_3_5_7
    from dzien_2.zad_9 import divided_by_and_3_5_7
    from dzien_2.zad_10 import is_leap_year
    from dzien_3.zad1 import table_print, create_list
    from dzien_3.zad2 import remainder_of_cash
    from dzien_3.zad3 import pyramid_draw
    from dzien_3.zad4 import dog_years

    print_programs_list()

    user_choice = None
    user_choice = check_if_good(user_choice, int, "Please provide number of program that you want to run: ")
    user_choice = int(user_choice)

    if user_choice == 1:
        celsius_to_fahrenheit()
        #print(celsius_to_fahrenheit.__doc__)
    elif user_choice == 2:
        fahrenheit_to_celsius()
    elif user_choice == 3:
        surface_area_of_circle()
    elif user_choice == 4:
        first_last()
    elif user_choice == 5:
        rectangle()
    elif user_choice == 6:
        binary_to_decimal_int()
    elif user_choice == 7:
        if_even()
    elif user_choice == 8:
        divided_by_or_3_5_7()
    elif user_choice == 9:
        divided_by_and_3_5_7()
    elif user_choice == 10:
        is_leap_year()
    elif user_choice == 11:
        table_print(create_list())
    elif user_choice == 12:
        remainder_of_cash()
    elif user_choice == 13:
        pyramid_draw()
    elif user_choice == 14:
        dog_years()
    else:
        print('Wrong number!')


multitool()



