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
		self.positive_vs_negative = {
			'Undetermined': {'correctas': 0, 'incorrectas': 0},
			'Non-USA': {'correctas': 0, 'incorrectas': 0},
			'World': {'correctas': 0, 'incorrectas': 0},
			'USA only': {'correctas': 0, 'incorrectas': 0}
		}
		#comparacion para calcular los exitos y los fracasos
		for i in range(len(s_list)): #len(s_list) = len(pred_list)
			if s_list[i][0] == pred_list[i][0]:
				self.correctos += 1

				if int(pred_list[i][0]) == 1:
					self.positive_vs_negative['Undetermined']['correctas'] += 1
				elif int(pred_list[i][0]) == 2:
					self.positive_vs_negative['Non-USA']['correctas'] += 1
				elif int(pred_list[i][0]) == 3:
					self.positive_vs_negative['World']['correctas'] += 1
				else:
					self.positive_vs_negative['USA only']['correctas'] += 1

			else:
				self.incorrectos += 1

				if int(pred_list[i][0]) == 1:
					self.positive_vs_negative['Undetermined']['incorrectas'] += 1
				elif int(pred_list[i][0]) == 2:
					self.positive_vs_negative['Non-USA']['incorrectas'] += 1
				elif int(pred_list[i][0]) == 3:
					self.positive_vs_negative['World']['incorrectas'] += 1
				else:
					self.positive_vs_negative['USA only']['incorrectas'] += 1


		for i in range(len(pred_list)):
			if int(pred_list[i][0]) == 1:
				self.ocurrencias['Undetermined'] += 1
			elif int(pred_list[i][0]) == 2:
				self.ocurrencias['Non-USA'] += 1
			elif int(pred_list[i][0]) == 3:
				self.ocurrencias['World'] += 1
			else:
				self.ocurrencias['USA only'] += 1

		#mrr
		for i in range(len(pred_list)):
			true_clase = int(s_list[i][0])
			clase_pointer = float(pred_list[i][1:].split()[true_clase-1])
			predictions = map(lambda x: float(x), pred_list[i][1:].split())
			predictions.sort(reverse=True)
			index = predictions.index(clase_pointer)+1
			self.mrr += 1.0/float(index)
		self.mrr /= 200.0

		
			



"""

Te recomiendo lo saques para el total de datos (concatena los resultados)
para sacar MRR debes utilizar tus etiquetas y no las que estan en el archivo predictions.dat

1 0.25 0.5 0.1 0.15
Donde 1 es tu etiqueta y el resto son las probabilidades del archivo, 
ahora debes ubicar la probabilidad dada por tu etiqueta, osea, para la etiqueta 1 es la prob 0.25.

Luego, ordenas de mayor a menor las probabilidades:

0.5 0.25 0.15 0.1

Y ves que que ubicacion quedo, que en este caso es la segunda, por ende tu reciproco es 1/2
"""
