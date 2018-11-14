# Script that is going to say 'Hello' to you!

name = input("Podaj swoje imię:\n")


def hello_function(t):
    print(f'Cześć {t.capitalize()}!')


hello_function(name)
