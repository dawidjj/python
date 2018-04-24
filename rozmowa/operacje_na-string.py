napis = "jakis tekstaaa"
print(len(napis)) # długośc napisu w tym wypadku 11
print(napis.index('a')) # zwrócenie pod jakim indeksem znajduje się a, jeśli jest więcej a w tekście to zwraca tylko pierwsze wystąpienie
print(napis.count('a')) # sprawdza ile razy pojawiło się wystąpienie ciągu "a" w zmiennej
print(napis[2]) # dostęp do pojedynczego znaku jeśli znamy jego indeks
print(napis[:]) # napis[:] i napis[::] wypisze cały tekst
print(napis[0:3]) #wyświetli jak bo zaczynamy od indeksu 0 ale kończymy na 2 bo 3 oznacza, że indeksu 3 nie wypisujemy
#napis[0:3] == napis[:3]
print(napis[3:]) #jeśli nie ma którejś liczby przed : lub za : to domyślnie brane jest od początku lub do końca
print(napis[-1]) #jeśli użyjemy ujemnego indeksu to znaki będą liczone od końca
print(napis[-4:-2]) # wiświetli ta
print(napis[0:10:1]) # trzecia liczba oznacza co ile znaków ma czytać
print(napis[::-1]) # oznacza, że czyta od końca

print('dawid',napis[2:-3])