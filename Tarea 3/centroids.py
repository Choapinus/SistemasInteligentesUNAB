from math import log

class Metrics():
	def __init__(self, key, value, total):
		try:
			self.name = key
			self.entropy = float(value)/float(total)*log(float(value)/float(total), 2)*-1.0
			self.purity = float(value)/float(total)
			self.precision = self.purity
			self.recall = float(value)/2000.0
			self.f1_score = (2.0*self.precision*self.recall)/(self.precision+self.recall)
		except ValueError:
			pass
		except Exception:
			print 'gg in centroids.py'


class Centroid():
	def __init__(self, cent):
		self.name = cent.split()[0]
		self.data = cent.split()[1:]
		self.metrics = []
		self.etiquetas = {
			'Undetermined': 0,
			'Non-USA': 0,
			'World': 0,
			'USA only': 0
		}

		for i in range(len(self.data)):
			if self.data[i] == '1':
				self.etiquetas[self.etiquetas.keys()[0]] += 1
			elif self.data[i] == '2':
				self.etiquetas[self.etiquetas.keys()[1]] += 1
			elif self.data[i] == '3':
				self.etiquetas[self.etiquetas.keys()[2]] += 1
			elif self.data[i] == '4':
				self.etiquetas[self.etiquetas.keys()[3]] += 1
			else:
				raise KeyError("Existe una etiqueta que no corresponde")

		for key, value in self.etiquetas.items():
			self.metrics.append(Metrics(key, value, sum(self.etiquetas.values())))


