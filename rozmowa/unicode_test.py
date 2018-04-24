"""
https://www.slideshare.net/robertzaremba/python-io-14451136
"""
import sys

s = "Jalapeño"
data = s.encode('utf-8')
print(data)

data2 = data.decode('utf-8')
print(data2)

a = "Jalape\xf1o"
b = "Jalapen\u0303o"
print(a,b, a == b, len(a), len(b))

#definiowanie separatora
print(1,2,3, sep=":")

#deifniowanie koniec lini
print('dawid', 'dd', end="!")
#sys.stdout().write()

price = 20

#python2
s = "%.4f" % price
print(s)

#python3
s = format(price, '.3f')
print(s)

print("{0} has{1} dsdsds {text}".format("Dawid", "Anna", text='kwadrat'))
print("To jest {} i ma {}". format("Dawid", 28))

s = ('ACME',20,23.40)
#pojedyncze zagnieżdżanie ale mi nie działa
#print("{0:{zmienna}s}{2}".format(*s, zmienna = 'szerokosc'))

#przekazywanie slownika w format_map
print("{name} has {mess} message".format_map({
    'name': 'Dawid',
    'mess': 3
}))

from string import Template
msg = Template("name hasn messages")
print(msg.substitute(name = 'Dawid'))


wyraz = "Dawid s"
print(wyraz.split('a'))
print(wyraz.upper())
print(wyraz.lower())

record = {'Name': 'Dawid', "Age": 28}
print('My name is {r[Name]} and I have {r[Age]}'.format(r=record))

lista = [2,4,5,6]

print(lista)
lista.append(6)
print(lista)
lista.extend([4,7])
print(lista)