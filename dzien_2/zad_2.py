# Simple converted from Fahrenheit degrees to Celsius degrees

print(
    'Hello in the simple degrees converter! \nThis program is converting degrees from Fahrenheit scale to Celsius one.')

fahrenheit = input("Please provide value of Fahrenheit degrees: ")
pattern = (int(fahrenheit)-32)/1.8
print(f'Following pattern is going to be used for conversion: (℉-32)/1.8.')


def choice():
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


choice()
