import csv
from etiquetas_class import Etiqueta


def clasificar(archivo_csv = 'data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', lista_textos_perfiles=None):
	with open(archivo_csv, 'rb') as f:
		reader = csv.reader(f)
		data = list(reader)
		
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