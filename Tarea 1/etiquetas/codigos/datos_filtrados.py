import csv, sys, pyperclip, math
from etiquetas_class import Etiqueta
from functions import calcularPaises, save_data, entropia_paises


"""
TODO:
meter texto de perfil en objeto Etiqueta (para la tarea 2 piden contar palabras)
archivo .dat se lee con open(nombre, 'r'), splitear por '\n' y se obtiene un string con id y perfil en html

solo resta sacar la info mutua
pd: sacar el pyperclip o instalarlo por codigo para que no tire error
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
		print 'Cantidad en '+et+':', len(etiquetas[et])
		print 'Probabilidad de '+et+':', float(len(etiquetas[et]))/2000.0
		print
		string += '{name:\''+et+'\', y:'+str(len(etiquetas[et]))+'}'
	string += ']'
	
	#pyperclip.copy(string)


	#entropy calculation
	entropy = 0

	for etiqueta in etiquetas:
		#print 'entropy ', etiqueta, math.log(float(len(etiquetas[etiqueta]))/2000, 2)
		pr = float(len(etiquetas[etiqueta]))/2000.0
		entropy += pr*math.log(pr, 2)*-1
		print 'Entropia de '+etiqueta+':', pr*math.log(pr, 2)*-1

	print '\nentropy:', entropy
	print



	paises_calculados = []

	paises_calculados.append(calcularPaises('World', etiquetas['World'], etiquetas))
	paises_calculados.append(calcularPaises('USA only', etiquetas['USA only'], etiquetas))
	paises_calculados.append(calcularPaises('Non-USA', etiquetas['Non-USA'], etiquetas))

	#guardar archivos en txt y csv para graficas
	save_data(paises_calculados)


	#entropias en terminos de ubicacion geografica
	#print paises_calculados[0]
	
	entropia_paises(etiqueta='World', dict_paises=paises_calculados[0])
	entropia_paises(etiqueta='USA only', dict_paises=paises_calculados[1])
	entropia_paises(etiqueta='Non-USA', dict_paises=paises_calculados[2])
	
	#print entropia_paises(dict_paises=paises_calculados[0])

	



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