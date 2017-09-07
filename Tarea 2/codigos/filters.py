from bs4 import BeautifulSoup
import re
from etiquetas_class import Etiqueta, Perfil


def leer_csv(archivo_csv = 'data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', lista_textos_perfiles=None):
	arch = open(archivo_csv, 'r')
	data = arch.readlines()
	arch.close()
	del data[0] #data[0] => ['id_perfil;clase;lugares']

	etiquetas = {
	'USA only': [], 
	'Non-USA': [], 
	'World': [], 
	'Undetermined': []
	}

	#begin the clasification
	for element in data:
		if lista_textos_perfiles == None:
			obj = Etiqueta(element)
		else:
			#busqueda del id_perfil
			obj = Etiqueta(element)
			for perfil in lista_textos_perfiles:
				if obj.id_perfil == perfil.id_perfil:
					obj = Etiqueta(obj, perfil.texto, flag=True)

		etiquetas[obj.clase].append(obj)

	return etiquetas

def get_dat(archivo_csv='data/Perfiles-(a.valenzuelagonzlez@uandresbello.edu).dat'):
	perfiles = open(archivo_csv, 'r')
	perfiles = perfiles.readlines()

	#clean text from html tags
	for i in range(len(perfiles)):
		perfiles[i] = BeautifulSoup(perfiles[i], "html.parser").get_text()


	#lista de objetos Perfiles
	perfiles_texto = []
	for i in perfiles:
		perfiles_texto.append(Perfil(i))

	return perfiles_texto


def get_etiquetas(_csv=None, _dat=None):
	if _csv is None or _dat is None:
		return leer_csv(lista_textos_perfiles=get_dat())
	else:
		return leer_csv(_csv, lista_textos_perfiles=get_dat(_dat))


def get_stopwords(txt='data/stopwords.txt'):
	arch = open(txt, 'r')
	stopwords = arch.readlines()
	arch.close()

	for i in range(len(stopwords)):
		stopwords[i] = stopwords[i].replace('\n', '')

	return set(stopwords)

def only_alpha(etiquetas):
	regex = re.compile('[^a-zA-Z ]') #filtra todos los simbolos non-alpha, excepto los spaces
	for key in etiquetas.keys():
		for perfil in etiquetas[key]:
			perfil.texto = regex.sub('', perfil.texto)
			#string = regex.sub('', string) #ejemplo de uso
	return etiquetas

def get_words(etiquetas):
	words = set()
	stopwords = get_stopwords()
	for key in etiquetas.keys():
		for perfil in etiquetas[key]:
			for palabra in perfil.texto.split():
				words.add(palabra)
	
	words = words - stopwords

	return list(words)

"""
listo: obtener todas las palabras de todos los perfiles, set y luego list para tener el "id"
listo: borrar stopwords
listo: despues, contar las palabras para cada vector
crear metodo que tome la lista de todas las palabras, que ubique el id de la llave del dict de las palabras de cada vector y genere el vector
"""


