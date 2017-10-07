class Centroid():
	def __init__(self, cent):
		self.name = cent.split()[0]
		self.data = cent.split()[1:]
		self.etiquetas = {1:0, 2:0, 3:0, 4:0}

		for i in range(len(self.data)):
			if self.data[i] == '1':
				self.etiquetas[1] += 1
			elif self.data[i] == '2':
				self.etiquetas[2] += 1
			elif self.data[i] == '3':
				self.etiquetas[3] += 1
			elif self.data[i] == '4':
				self.etiquetas[4] += 1
			else:
				raise KeyError("Existe una etiqueta que no corresponde")