import csv
import json

content = []
jsonfile = open('./files/file.json', 'w')

with open('./files/iris.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')

    for row in data:
        content.append(row)

    json.dump(content, jsonfile)

#https://konradhalas.pl/media/slides/type-hints-w-jezyku-python-innowierstwo-czy-zbawienie.pdf
#https://4programmers.net/Forum/Kariera/265480-pytania_rekrutacyjne_python?p=1219869#id1219869