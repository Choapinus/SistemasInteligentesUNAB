import csv
import sys
import pyperclip
import math
import json
from difflib import SequenceMatcher
from etiquetas_class import Etiqueta

#compara dos strings y retorna un % de similitud
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

"""
TODO:
meter texto de perfil en objeto Etiqueta (para que?)
ver si se puede automatizar el calculo de la wea que te mando el jean (informacion mutua)
archivo .dat se lee con open(nombre, 'r'), splitear por '\n' y se obtiene un string con id y perfil en html
"""

with open('data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', 'rb') as f:
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
	
	pyperclip.copy(string)


	#entropy calculation

	entropy = 0

	for etiqueta in etiquetas:
		#print 'entropy ', etiqueta, math.log(float(len(etiquetas[etiqueta]))/2000, 2)
		Pr = float(len(etiquetas[etiqueta]))/float(2000)
		entropy += math.log(Pr)*-1*Pr

	print '\nentropy:', entropy




	#paises unicos
	#nota: deben estar etiquetados con una convencion
	country_count = set()
	for i in range(len(etiquetas['World'])):
		for j in etiquetas['World'][i].lugares:
			country_count.add(j)
	
	#imprimirlos
	#for i in country_count:
	#	print i


	#contar los paises para informacion mutua
	ccount = {}

	for i in country_count:
		ccount[i] = 0

	for i in range(len(etiquetas['World'])):
		for j in etiquetas['World'][i].lugares:
			ccount[j] += 1


	#guardar archivos en txt y csv para graficas
	ocurrencias = open('data/paises_txt.txt', 'w')

	print '\n'
	print 'Paises y numero de ocurrencias en World'
	for i in ccount:
		print i, ':', ccount[i]
		ocurrencias.write(i+': '+str(ccount[i])+'\n')

	ocurrencias.write('\n\njson object:\n')
	ocurrencias.write(json.dumps(ccount))

	with open('data/paises_csv.csv', 'wb') as csv_file:
		[csv_file.write('{0};{1}\n'.format(key, value)) for key, value in ccount.items()]

	print '\ndone'



	"""
	#show cute data
	for i in range(100):
		print 'perfil:', data[i]
		aux = Etiqueta(data[i])
		print 'object', i+1
		print 'id_perfil:', aux.id_perfil+'.'
		print 'clase:', aux.clase+'.'
		print 'lugares:', str(aux.lugares)+'.'
		print '\n'
	"""

sys.exit()


"""
entropy: https://www.youtube.com/watch?v=reNELmcKAhc
informacion mutua: https://www.youtube.com/watch?v=DSdcoDhZAt8

"""