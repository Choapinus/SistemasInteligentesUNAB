import csv
import sys
import pip

pip.main(['install', 'pyperclip'])

import pyperclip
import math
from etiquetas_class import Etiqueta


"""
filtrar cuanta data en % pertenece a cada clase
calcular entropia del dataset
"""

archivo = raw_input('ingrese nombre csv: ')

#with open('../Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', 'rb') as f:
with open(archivo, 'rb') as f:
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
	#entropy_world = math.log(float(len(etiquetas['World']))/2000, 2)
	
	#print '\ndone'
	#print 'entropy_world:',entropy_world*float(len(etiquetas['World']))/2000

	"""
	#show cute data
	for i in range(len(data)):
		print 'perfil:', data[i]
		aux = Etiqueta(data[i])
		print 'object', i+1
		print 'id_perfil:', aux.id_perfil+'.'
		print 'clase:', aux.clase+'.'
		print 'lugares:', str(aux.lugares)+'.'
		print '\n'
	"""

sys.exit()