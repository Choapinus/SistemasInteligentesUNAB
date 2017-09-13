class Vector():
	def __init__(self, s_list, pred_list):
		self.correctos = 0
		self.incorrectos = 0
		self.mrr = 0.0
		self.ocurrencias = {
			'Undetermined': 0,
			'Non-USA': 0,
			'World': 0,
			'USA only': 0
		}
		#comparacion para calcular los exitos y los fracasos
		for i in range(len(s_list)): #len(s_list) = len(pred_list)
			if s_list[i][0] == pred_list[i][0]:
				self.correctos += 1
			else:
				self.incorrectos += 1

		for i in range(len(s_list)):
			if int(s_list[i][0]) == 1:
				self.ocurrencias['Undetermined'] += 1
			elif int(s_list[i][0]) == 2:
				self.ocurrencias['Non-USA'] += 1
			elif int(s_list[i][0]) == 3:
				self.ocurrencias['World'] += 1
			else:
				self.ocurrencias['USA only'] += 1

		for i in range(len(pred_list)):
			if pred_list[i][0] != s_list[i][0]:
				clase = int(pred_list[i][0])
				clase_pointer = float(pred_list[i][1:].split()[clase-1])
				predictions = map(lambda x: abs(float(x)), pred_list[i][1:].split())
				predictions.sort(reverse=True)
				pred = predictions.index(clase_pointer)+1
				self.mrr += 1.0/float(pred)
			else:
				self.mrr += 1.0
			



"""
ahora... esas weas de numeros feos
debes ordenarlos de mayor a menor
y luego ver... en que posicion quedo, el que tu clasificador asigno
por ejemplo si dice
3 123 324 100
debes ordenar de mayor a menor y queda como
3 324 123 100
entonces... o sea.. antes de ordenar, debes ver que dice 3... y como dice 3.. eso apunta al 100
y luego ordenar... y despues de ordenar, ver donde quedo ese 100
entonces quedo en la posicoon 3
entonces debe ser 1/3
y eso es como 0.33
y asi con todas las etiquetas... y las sumas todas y luego divides por 2000 vualah.. sacas el MRR total xd


y que pasa con las predicciones que no aciertan?, se suman igual??
"""
