"""
__getattr__ - jest wywoływane gdy atrybut nie został znaleziony w klasie (lub w obiekcie). Krótko mówiąc jeśli chcesz żeby odwołanie do nieinstniejącego atrybutu robiło coś innego niż rzucało wyjątek AttributeError, zdefiniuj własną metodę __getattr__.

__getattribute__ - zwraca atrybut jeśli znajduje się w klasie (obiekcie), w przeciwnym przypadku rzuca wyjątek AttributeError. Po rzuceniu AttributeError jeśli klasa ma metode __getattr__ zostaje ona wywołana, w przeciwnym wypadku wyjątek ten przechodzi wyżej.

Potestuj to:

Kod
class C(object):
   x = None
   def __getattr__(self, name):
       print '__getattr__', name
       #raise AttributeError
   def __getattribute__(self, name):
       print '__getattribute__',name
       if name == 'whoops':
           raise AttributeError
       return object.__getattribute__(self, name)
   def metoda(self): pass

c = C()
c.x
print
c.metoda()
print
c.a
print
c.whoops
"""