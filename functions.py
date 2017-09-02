import json

#funcion para contar ocurrencia de cada pais
#nota: deben estar etiquetados con una convencion 
#(nombre completo pais, inicial con mayuscula, NO debe terminar con un espacio)
def calcularPaises(nombre_etiqueta, objeto, dict_etiquetas):
	#funcion reculia webiada weon oh
	country_count = set()
	
	for i in range(len(objeto)):
		if type(objeto[i].lugares) == list:
			for j in dict_etiquetas[nombre_etiqueta][i].lugares:
				country_count.add(j)
		else:
			country_count.add(objeto[i].lugares)
	
	ccount = {}

	for i in country_count:
		ccount[i] = 0

	for i in range(len(dict_etiquetas[nombre_etiqueta])):
		if type(dict_etiquetas[nombre_etiqueta][i].lugares) == list:
			for j in dict_etiquetas[nombre_etiqueta][i].lugares:
				ccount[j] += 1
		else:
			ccount[dict_etiquetas[nombre_etiqueta][i].lugares] += 1
	
	return ccount

#guardar archivos en txt y csv para graficas
def save_data(lista):
	with open('for_graphs/world_csv.csv', 'wb') as csv_file:
		[csv_file.write('{0};{1}\n'.format(key, value)) for key, value in lista[0].items()]

	with open('for_graphs/usa_only_csv.csv', 'wb') as csv_file:
		[csv_file.write('{0};{1}\n'.format(key, value)) for key, value in lista[1].items()]

	with open('for_graphs/non_usa_csv.csv', 'wb') as csv_file:
		[csv_file.write('{0};{1}\n'.format(key, value)) for key, value in lista[2].items()]


	ocurrencias = open('for_graphs/world_txt.txt', 'w')

	for i in lista[0]:
		ocurrencias.write(i+': '+str(lista[0][i])+'\n')

	ocurrencias.write('\n\njson object:\n')
	ocurrencias.write(json.dumps(lista[0]))
	ocurrencias.close()


	ocurrencias = open('for_graphs/usa_only_txt.txt', 'w')

	for i in lista[1]:
		ocurrencias.write(i+': '+str(lista[1][i])+'\n')

	ocurrencias.write('\n\njson object:\n')
	ocurrencias.write(json.dumps(lista[1]))
	ocurrencias.close()


	ocurrencias = open('for_graphs/non_usa_txt.txt', 'w')

	for i in lista[2]:
		ocurrencias.write(i+': '+str(lista[2][i])+'\n')

	ocurrencias.write('\n\njson object:\n')
	ocurrencias.write(json.dumps(lista[2]))
	ocurrencias.close()