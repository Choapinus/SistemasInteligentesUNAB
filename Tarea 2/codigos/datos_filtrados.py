from bs4 import BeautifulSoup
from etiquetas_class import Etiqueta
from etiquetas_class import Perfil

def leer_csv(archivo_csv = 'data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', lista_textos_perfiles=None):
	data = open(archivo_csv, 'r')
	data = data.readlines()
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

def asociar_texto(archivo_csv='data/Perfiles-(a.valenzuelagonzlez@uandresbello.edu).dat'):
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


def clasificar(_csv=None, _dat=None):
	if _csv is None or _dat is None:
		return leer_csv(lista_textos_perfiles=asociar_texto())
	else:
		return leer_csv(_csv, lista_textos_perfiles=asociar_texto(_dat))