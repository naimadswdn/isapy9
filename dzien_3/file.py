import string

print(string.ascii_lowercase)
zmienna = string.ascii_lowercase

#for i in zmienna:
#    print(i)


liczba = 1.33333
print('%06.4f' % liczba)

liczyb = range(3,8)

print(type(liczyb))



lista1 = [1, 2, 3]
lista2 = ['kwiatek', 'doniczka', 'ziemia', 'woda']
lista3 = []
lista4 = [1, 'dwa', 3, 4]
lista5 = list('dwa')
lista6 = list('1')

del(lista5[1])
# print(lista5)
#
# lista7 = [lista1, lista2, lista4]
# print(lista7)
# print(lista7[1][2][0])
#
#
# krotka1 = (1,2,3)
# print(krotka1)

a,b,c,d,e = liczyb

print(a,b,c,d,e)

print(*liczyb)

print(*range(1,11))


x = None
while x != 't':
    x = input('Napisz "t". ')
    if x == 't':
        print('Brawo!')
        break
    else:
        print('To nie jest t!')
        continue


x = lambda a : a + 10
print(x(5))
