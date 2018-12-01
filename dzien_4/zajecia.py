
# numbers = range(0, 51)


# for number in numbers:
#     if number % 2 != 0:
#         continue
#     print(number)


# text = 'Ala ma kota'
# #
# for i in text:
#     print(i)


to_buy_list = ['chleb', 'mleko', 'woda']

name_list = ['Ola', 'Ala', 'Tomek', 'Jan', ['1', '2']]

# for i, name in enumerate(name_list):
#     print(f'On {i} there is assigned name: {name}')

# enumerate wyświetla numer każdego "name" for pętli for

surname_list = ['Kowalska', 'Malinowska', 'Iksiński', 'Igrekowski']

# for a, b, c in zip(name_list, surname_list, to_buy_list):
#     print(a, b, c)
#
#
# for a, b in zip(name_list, surname_list):
#     print(a, b)

# zip pozwala wywowyływać elementy o tym samym indeksie z dwóch różnych list
# gdy podam jeden parametr dla dwóch list to robi krotkę z dwoma elementami

# inty i stringi nie sa zmiennymi referencyjnymi!! listy sa!


#REFERENCJE

new_name_list = name_list # przypisanie - tworzy referencję!

# how to create a copy of list:
new_name_list = name_list.copy() # funkcja copy, kopiuje listę
new_name_list = list(name_list) # konstrutor list zawsze tworzy nowy element, nie referencję!
new_name_list = name_list[:] #indeksowanie - omija początek i koniec i tworzy na tej podstawie nową liste

name_list.append('Damian')
#
# print(name_list)
# print(new_name_list)


#how to create with import copy:
import copy

name_list.append(surname_list)

lista = ['AAA', ['BBB', ['CCC']]]

lista_przypisanie = lista
lista_copy = copy.copy(lista)
lista_deepcopy = copy.deepcopy(lista)

lista[1][0] = 'YYY'

# print(lista)
# print(lista_przypisanie)
# print(lista_copy)
# print(lista_deepcopy)

# deepcopy kopiuje rownież zagnieżdzone listy w liscie! a copy nie!
# czyli w kazdym z 3 pierwszych przypadkow powyżej zamiana lista[1][0] = 'YYY' spowoduje podmienienie 'BBB' na 'YYY' bo to jest referencją
# a lista_deepcopy bedzie nie zmieniona! :)

# FUNKCJE TEŻ SĄ REFERENCYJNE!

import re

def how_many(digit, string):
    string = string.casefold()
    #print(string)
    value = string.count(digit)
    return value

print(how_many('a', 'DamiAAn'))





