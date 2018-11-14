# Script that is going to say 'Hello' to you!

name = input("Podaj swoje imię:\n")
name = name.strip(' ')  # removing spaces from user string
signs = len(name)
last_sign = name[signs - 1] # can be replaced with name[-1:]


def hello_function(t):
    if last_sign=='a':
        print(f'Cześć {t.capitalize()}! Jesteś kobietą.')
    else:
        print(f'Cześć {t.capitalize()}! Jesteś mężczyzną.')
    print(f'Twoje imię ma {signs} znaków.')
    print(f'Ostatnia litera imienia to {last_sign}.')


hello_function(name)
