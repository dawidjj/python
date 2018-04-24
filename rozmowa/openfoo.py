"""
obiekt zwracany przez open różni się w zależności od przekazanego parametru mode
"""

file = open('./files/foo.txt',"rt")
print(file)
#<_io.TextIOWrapper name='./files/foo.txt' mode='rt' encoding='UTF-8'>

file2 = open('./files/foo.txt', "rb")
print(file2)
#<_io.BufferedReader name='./files/foo.txt'>

file3 = open('./files/foo.txt', "rb", buffering=0)
print(file3)
#<_io.FileIO name='./files/foo.txt' mode='rb' closefd=True>

import io
import os
f = io.FileIO("./files/foo.txt", "r")
data = f.read(1)
f.seek(16384, os.SEEK_SET)
print(data)

for line in open('./files/foo.txt', encoding="utf-8"):
    print(line.split())

zmienna = "dawidos"
print(zmienna[-2])