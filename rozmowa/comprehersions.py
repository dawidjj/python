import pprint

lista = [n ** 2 for n in range(10) if n % 2 == 0]
print(lista)
print(type(lista))

zbior = {n ** 2 for n in range(10)}
print(zbior)
print(type(zbior))

slownik = {n:n ** 2 for n in range(10)}
print(slownik)
print(type(slownik))

multiplication_table = {n: {x: x * n for x in range(1,11)} for n in range(1,11)}
pprint.pprint(multiplication_table)

# tupola = (n ** 2 for n in range(10))
# print(tupola)
# print(type(tupola))

x = 5
y = 10
x, y = y, x
print(x,y)

_,_,_ = [1,2,3]
print(_)
a, *b, c = [1, 2, 3, 4, 5]
print(a,b,c)

print(get_rows([1, 2, 3, 4, 5], 2))