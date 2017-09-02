import csv
import sys
import pyperclip
import math
from etiquetas_class import Etiqueta
from functions import calcularPaises, save_data

"""
TODO:
meter texto de perfil en objeto Etiqueta (para la tarea 2 piden contar palabras)
archivo .dat se lee con open(nombre, 'r'), splitear por '\n' y se obtiene un string con id y perfil en html

solo resta sacar la info mutua
"""

with open('to_read/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', 'rb') as f:
	reader = csv.reader(f)
	data = list(reader)
	
	del data[0] #data[0] => ['id_perfil;clase;lugares']

	etiquetas = {
	'USA only': [], 
	'Non-USA': [], 
	'World': [], 
	'Undetermined': []
	}

	string = '['

	#begin the clasification
	for element in data:
		perfil = Etiqueta(element)
		etiquetas[perfil.clase].append(perfil)

	#just for the pie graph, ademas de que muestra los datos de manera entendible
	for et in etiquetas:
		if len(string) != 1:
			string += ','
		print 'cantidad de elementos en '+et+':', len(etiquetas[et])
		string += '{name:\''+et+'\', y:'+str(len(etiquetas[et]))+'}'
	string += ']'
	
	#pyperclip.copy(string)


	#entropy calculation

	entropy = 0

	for etiqueta in etiquetas:
		#print 'entropy ', etiqueta, math.log(float(len(etiquetas[etiqueta]))/2000, 2)
		pr = float(len(etiquetas[etiqueta]))/2000.0
		entropy += pr*math.log(pr, 2)*-1

	print '\nentropy:', entropy



	paises_calculados = []

	paises_calculados.append(calcularPaises('World', etiquetas['World'], etiquetas))
	paises_calculados.append(calcularPaises('USA only', etiquetas['USA only'], etiquetas))
	paises_calculados.append(calcularPaises('Non-USA', etiquetas['Non-USA'], etiquetas))

	#guardar archivos en txt y csv para graficas
	save_data(paises_calculados)

	print '\nall done'
	
	#calcular info mutua	



	



sys.exit()


"""
entropy: https://www.youtube.com/watch?v=reNELmcKAhc
informacion mutua: https://www.youtube.com/watch?v=DSdcoDhZAt8

para la informacion mutua:
sacar paises no repetidos de cada etiqueta excepto undetermined
luego, calcular cuantos paises de cada uno hay en cada etiqueta

"""