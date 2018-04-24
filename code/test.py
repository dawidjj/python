#http://python.astrotech.io/
#wyświetlanie na ekran
print("Hello World")

variableInt = 5
#sprawdzanie typu zmiennej
print(type(variableInt))


#tworzenie zmiennej typu float na dwa sposoby
variableFloat = 4.3
print(type(variableFloat))

variableFloat2 = float(4)
print(variableFloat2)

#wyświetlanie większje precyzji zmiennej float
print ('%.20f' % variableFloat2)

#łączenie stringów tak samo jak dodwanie liczb
x = 1;
y = 1;
a = 'test'
b = 'dddd'
print(x+y)
print(a + ' ' + b)

# sprawdzenie jakiego typu jest zmienna
print(isinstance(a, float))
print(isinstance(variableFloat2, float))

#w pythonie nie ma tablic tylko są listy
emptylist = list() #tworzenie pustej listy
emptyList2 = []
list1 =  ['sss', 2, '4434', a]
list1[3] = 'zmiana'
# list1[4] = 'gh' tak nie można zrobić bo nie ma 4 indeksu
print(emptylist, emptyList2, list1[3])

#dołączanie czegoś do listy jako jeden index
list1.append([45,6])
print(list1)

#dołączanie tych elementów do tablicy jako kolejne indeksy
list1.extend([9,11, [2,3]])
print(list1)

#usuwanie elementu z listy
del (list1[4])
print(list1)

#python przestrzega kolejność działania i nie trzeba używać nawiasów
suma = 1 + 2 * 3 / 4.0

#symbol potęgowania
kwadrat = 2**2
print(kwadrat)
szescian = 2**3
print(szescian)

#powielanie tego samego tekstu
wiele = 'a' * 10
print(wiele)
print(wiele * 2)

#powielanie elementów w tablicy
print([3,4,2,'fg'] * 3)

#liczba wystąpień elementu w tablicy
print(list1.count(9))

#liczba elementów w tablicy
print(len(list1))

d = object()
print(d)

#ostatni element
print(list1[-1])

odwrotnie = "annakoralewska"
print(odwrotnie[2:-2])

string = "testowystring"
print(string[0:10]) #testowystr
print(string[1:-5]) #estowys
print(string[::-1]) #gnirtsywotset
print(string[5:0:-1]) #wotse
print(float('   -12345\t'))
print(float('1e2')) #100.0
print(float('1e-003')) #0.001
d = str(5) #zwraca łańcuch znaków (string)
print(type(d))

print(b)
name = input('Podaj imie: '); #pobieranie znaków od użytkownika z konsoli
print(name)
STALA = 5
print(STALA)
STALA = 6
print(STALA)

#https://www.slideshare.net/wlichota/jak-przygotowa-si-do-rozmowy-rekrutacyjnej-na-python-developera
#http://www.learnpython.org/pl/Formatowanie_Napisow

# print("Hello World")
#
# x = 10
# print(x)
#
# y = 5
# print(y)
#
# print(type(y))
#
# y = y/5
# print(y)
# print(type(y))
#
#
# zmienna1 = "Hello World"
#
# # wyświeli na ekranie 2 razy hellow world
# print(zmienna1 * 2)
#
# zmienna2 = zmienna1 + " yay"
# print(zmienna2)
#
# #python 2.7 raw_input w 3.5 zmieniono na samo input
#
# # pobieranie tego co poda użytkownik z klawiatury
# # x = input()
#
# # x = int(x)
# # print(x)
#
# x = "Alaa ma kota, Kot ma Ale"
# print(x[0:4]) #Alaa
# print(x[:4]) #Alaa
#
# print(x[:])
# print(x[::-1])