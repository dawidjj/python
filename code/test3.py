import obiekt

newTest = obiekt.Test()
newTest.variable = 8

newTest.hello()

def monkey_patch():
    print('hhh')

newTest.hello = monkey_patch
newTest.hello()

newTest2 = obiekt.Test()
newTest2.hello()

obiekt.Test.statyczna()

newTest3 = obiekt.Test()
print(newTest3)

class FooClass:
    pass



try:
    f = FooClass()
    raise NameError('Zwracam error')
    #print(isinstance(f, FooClass))
    #print(isinstance(FooClass, type))
except NameError as error:
    print(error)
    print('Błąd złapany')
else:
    print('Nie było błędu')
finally:
    print('To wykonuje się na końcu nie ważne czy jest jakiś błąd czy nie')
# obiekt.Test.hello = monkey_patch
# newTest3 = obiekt.Test()
# newTest3.hello()

FILENAME = 'plik'

try:
    with open(FILENAME) as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Brak uprawnien')
