# Simple converted from Celsius degrees to Fahrenheit degrees


def Celsiusz_to_Fahrenheit():
    """Hello in the simple degrees converter!.
    This program is converting degrees from Celsius scale to Fahrenheit one."""

    celsius = input("Please provide value of Celsius degrees: ")
    pattern = int(celsius) * 1.8 + 32

    print(f'Following pattern is going to be used for conversion: ℃*1.8+32.')
    print('Please write "y" if you would like to see calculations step by step. Write "n" if you want only result')
    while True:
        user_choice = input()
        if user_choice == 'y':
            print(f'Step one: substitution of your value to the pattern: \n℉={celsius}*1.8+32')
            print('Step two: calculating results..')
            print(f'Result: {celsius}℃ is equal to {round(pattern,2)}℉.')
            break
        elif user_choice == 'n':
            print(f'Result: {celsius}℃ is equal to {round(pattern,2)}℉.')
            break
        else:
            print('Wrong answer! Please write "y" or "n".')
            continue


Celsiusz_to_Fahrenheit()