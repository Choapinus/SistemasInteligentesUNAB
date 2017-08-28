import csv
import sys
import pyperclip
import math
from difflib import SequenceMatcher
from etiquetas_class import Etiqueta

#compara dos strings y retorna un % de similitud
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

"""
TODO:
meter texto de perfil en objeto Etiqueta (para que?)
ver si se puede automatizar el calculo de la wea que te mando el jean (informacion nosequewea)
archivo .dat se lee con open(nombre, 'r'), splitear por '\n' y se obtiene un string con id y perfil en html
"""

with open('data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', 'rb') as f:
	reader = csv.reader(f)
	data = list(reader)
	#print data[0] #['id_perfil;clase;lugares']
	#aux = Etiqueta(data[154]) # 154 = world
	del data[0]

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

	#just for the pie graph
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
		entropy += math.log(float(len(etiquetas[etiqueta]))/2000, 2)*-1

	print 'entropy:', entropy

	country_count = set()

	#for i in range(len(etiquetas['World'])):
		#print etiquetas['World'][i].lugares
		

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
