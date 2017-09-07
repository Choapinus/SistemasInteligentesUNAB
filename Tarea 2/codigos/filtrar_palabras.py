from bs4 import BeautifulSoup
from datos_filtrados import clasificar

stopwords = open('data/stopwords.txt', 'r')
stopwords = stopwords.readlines()

for i in range(len(stopwords)):
	stopwords[i] = stopwords[i].replace('\n', '')

stopwords = set(stopwords)

#etiquetas = clasificar(_csv='nombre.csv', _dat='nombre.dat')

etiquetas = clasificar()

#se pudo ctm!!
print etiquetas[etiquetas.keys()[1]][0].lugares






"""
instalar bs4 con pip
TODO: contar palabras de cada texto
problema: en las palabras apareceran los puntos, las comas, los guines, todo... filtrar pls
string.split(sin parametros) -> retorna el string spliteado, podrias filtrar cada palabra o filtrar el texto entero
"""