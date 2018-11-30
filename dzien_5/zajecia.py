
dictionary = {
    "name": ["Łukasz", "Ala", "Ola", "Damian"],
    "surname": ["Falkowicz", 'Kowalska', 'Malinowska', 'Seredyn']
}

cities = {
    'city': ['Warszawa', 'Gdańsk', 'Sopot', 'Kraków']
}

# dictionary.update(city)
# print(dictionary)

# print(type(dictionary))
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())
#
# for key, item in dictionary.items():
#     print(key)
#     for i in item: # ITEM JEST JUZ CAŁĄ LISTĄ!
#         print(f'-> {i}')
#
# DOSTEP DO LISTY ZE SLOWNIKA: SLOWNIK['KLUCZ'] I WTEDY MAMY LISTE!!
#
# surname = dictionary["surname"]
#
# for i in surname:
#     print(i)
#
# for index, name in enumerate(dictionary["name"]):
#     surname = dictionary["surname"][index]
#     city = dictionary['city'][index]
#     print(f'My name is {name} {surname} and I am from {city}')

#
# for index, name in enumerate(dictionary["name"]):
#     surname = dictionary["surname"][index]
#     city = cities['city'][index]
#     print(f'My name is {name} {surname} and I am from {city}')
#

# file = open('dane.txt', "r")
# print(file.read())
# # file.seek(1)
# # file.write('Damian')
# # file.seek(0)
# # print(file.read())
# file.close()

# file = open('dane.txt', "w")
# file.write('1')


# with open('dane.txt', "r+") as file:
#     # file = open('dane.txt', "r+")
#     i = file.readline()
#     i = int(i)
#     i += 1
#     print(i)
#     file.seek(0)
#     file.write(str(i))
#     file.close()


name = input('Please provide name: ')
text = input('Provide text: ')
with open('dane.txt', "a+") as file:
    file.write(name + " " + text + "\n")
    file.seek(0)
    print(file.read())

