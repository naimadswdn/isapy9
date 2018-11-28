# Simple converted from Fahrenheit degrees to Celsius degrees


def fahrenheit_to_celsius():
    """This program is converting degrees from Fahrenheit scale to Celsius one."""
    import time
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello in the simple Fahrenheit to Celsius degrees converter!')
    time.sleep(1.5)

    fahrenheit = None
    fahrenheit = check_if_good(fahrenheit, float, 'Please provide value of Fahrenheit degrees: ')

    # while True:
    #     fahrenheit = input("Please provide value of Fahrenheit degrees: ")
    #
    #     try:
    #         fahrenheit = float(fahrenheit)
    #         break
    #     except:
    #         print('Wrong data format! Did you provide a number?')
    #         continue

    pattern = (float(fahrenheit) - 32) / 1.8
    print(f'Following pattern is going to be used for conversion: (℉-32)/1.8.')

    print('Please write "y" if you would like to see calculations step by step. Write "n" if you want only result')
    while True:
        user_choice = input()
        if user_choice == 'y':
            print(f'Step one: substitution of your value to the pattern: \n℃=({fahrenheit}-32)/1.8')
            print('Step two: calculating results..')
            print(f'Result: {fahrenheit}℉ is equal to {round(pattern,2)}℃.')
            break
        elif user_choice == 'n':
            print(f'Result: {fahrenheit}℉ is equal to {round(pattern,2)}℃.')
            break
        else:
            print('Wrong answer! Please write "y" or "n".')
            continue
    repeat_y_or_n(fahrenheit_to_celsius, "Would you like to convert another Fahrenheit degree?")


fahrenheit_to_celsius()
