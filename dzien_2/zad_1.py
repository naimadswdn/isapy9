# Simple converted from Celsius degrees to Fahrenheit degrees

print(
    'Hello in the simple degrees converter! \nThis program is converting degrees from Celsius scale to Fahrenheit one.')

celsius = input("Please provide value of Celsius degrees: ")
pattern = int(celsius) * 1.8 + 32
print(f'Following pattern is going to be used to convert: ℃*1.8+32.')


def choice():
    print('Please write "y" if you would like to see calculations step by step. Write "n" if you want only result')
    while True:
        user_choice = input()
        if user_choice == 'y':
            print(f'Step one: substitution of your value to the pattern: \n℉={celsius}*1.8+32')
            print('Step two: calculating results..')
            print(f'Result: {celsius}℃ is equal to {pattern}℉.')
            break
        elif user_choice == 'n':
            print(f'Result: {celsius}℃ is equal to {pattern}℉.')
            break
        else:
            print('Wrong answer! Please write "y" or "n".')
            continue


choice()
