# Simple converted from Celsius degrees to Fahrenheit degrees



def Celsiusz_to_Fahrenheit():
    """This program is converting degrees from Celsius scale to Fahrenheit one."""
    import time
    from dzien_2.check_if_good import check_if_good

    print('Hello in the simple Celsius to Fahrenheit degrees converter!')
    time.sleep(1.5)

    celsius = None
    celsius = check_if_good(celsius,float,"Please provide value of Celsius degrees: ")

    # while True:
    #     celsius = input("Please provide value of Celsius degrees: ")
    #
    #     try:
    #         celsius = float(celsius)
    #         break
    #     except:
    #         print('Wrong data format! Did you provide a number?')
    #         continue

    pattern = float(celsius) * 1.8 + 32

    print(f'Following pattern is going to be used for conversion: ℃*1.8+32.')
    print('Please write "y" if you would like to see calculations step by step. Write "n" if you want only result.')
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
