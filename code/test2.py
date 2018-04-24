# # name = 'sJosé Jiménez'
# #
# # if name.startswith('José'):
# #     print('My name José Jiménez')
# # else:
# #     print('Noname')
#
# # s = {1,2} - {2}
# # print(set([2,3]))
#
# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
# #print(text.split('.'))
#
# for i in text.split('.'):
#     print(len(i))
#
# print(5//2)
#
# cyfry = [x for x in range(0,10) if x >2]
# print(cyfry)
#
# line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'
#
# d = [record for record in line.split(':') if record.startswith('/')]
# print(d)
#
# def podziel(a, b):
#     return a/b
# print(podziel(b=2, a=3))
# # print(a)

def argskwargs(a,b,c,d, *args, **kwargs):
    print(kwargs, args)
    #print(locals())

argskwargs(1,2,3,4,5,6,[6,7],dupa=3, cyc = {3: 4})

def liczby_0_do_5():
    return range(0, 5)

jeden, dwa, *reszta = liczby_0_do_5()

print(jeden, dwa, reszta)

import keyword as c
print(c.kwlist)
from keyword import kwlist as dupa
print(dupa)

print(__file__)
print(__name__)

import logging

log = logging.getLogger(__name__)
print(log)

#sorted() # operator niemutowalny nie zmienia listy

from pprint import pprint

data = [{'first_name': 'José', 'last_name': 'Jiménez'}, {'first_name': 'Max', 'last_name': 'Peck'}, {'first_name': 'Ivan', 'last_name': 'Ivanovic'}]

pprint(data)

def ehlo_world():
    """
    >>> ehlo_world()
    'ehlo world'
    """
    napis = 'ehlo world'
    return napis

if __name__ == '__main__':
    import doctest
    doctest.testmod()

class Pojazd:
    def zatrab(self):
        raise NotImplementedError

class Motor(Pojazd):
    def zatrab(self):
        print('bip')

class Samochod(Pojazd):
    pass
    def zatrab(self):
        pass
        print('biiiip')

obj = Motor()
obj.zatrab()

obj = Samochod()
obj.zatrab()


class Test:
    def __init__(self):
        self._variable = 5

    @property
    def variable(self):
        print('sssss')
        return self._variable

    @variable.setter
    def variable(self, data):
        print('ustawiam')
        self._variable = data

    @variable.deleter
    def variable(self):
        print('usuwam')
        del self._variable

print('jestem')
newTest = Test()
newTest.variable = 8
#print(newTest.variable)