from bs4 import BeautifulSoup
from datos_filtrados import clasificar
from etiquetas_class import Perfil

stopwords = open('data/stopwords.txt', 'r')
stopwords = stopwords.readlines()

for i in range(len(stopwords)):
	stopwords[i] = stopwords[i].replace('\n', '')

stopwords = set(stopwords)

perfiles = open('data/Perfiles-(a.valenzuelagonzlez@uandresbello.edu).dat', 'r')
perfiles = perfiles.readlines()

#clean text from html tags
for i in range(len(perfiles)):
	perfiles[i] = BeautifulSoup(perfiles[i], "html.parser").get_text()


#lista de objetos Perfiles
perfiles_texto = []
for i in perfiles:
	perfiles_texto.append(Perfil(i))

etiquetas = clasificar(lista_textos_perfiles=perfiles_texto)

#se pudo ctm!!
print etiquetas[etiquetas.keys()[0]][1].id_perfil, etiquetas[etiquetas.keys()[0]][1].texto





"""
instalar bs4 con pip
TODO: contar palabras de cada texto
problema: en las palabras apareceran los puntos, las comas, los guines, todo... filtrar pls
string.split(sin parametros) -> retorna el string spliteado, podrias filtrar cada palabra o filtrar el texto entero
"""