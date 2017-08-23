class Etiqueta():
	def __init__(self, perfil):
		if len(perfil) == 1:
			#print 'from if:',perfil
			perfil = perfil[0].split(';')
			self.id_perfil = perfil[0]
			self.clase = perfil[1].replace('"', '')
			self.lugares = perfil[2].replace('"', '')
		else:
			#print 'from else:',perfil
			perfil[0] = perfil[0].split(';')
			self.id_perfil = perfil[0][0].replace('"', '')
			self.clase = perfil[0][1].replace('"', '')
			self.lugares = [perfil[0][2].replace('"', '')]
			if self.lugares[0].startswith(' '):
				self.lugares[0] = self.lugares[0][1:]
			if self.lugares[0].endswith(' '):
				self.lugares[0] = self.lugares[0][:-1]
			for iterator in perfil:
				if type(iterator) != list:
					if iterator.startswith(' '):
						iterator = iterator[1:]
					if iterator.endswith(' '):
						iterator = iterator[:-1]
					self.lugares.append(iterator.replace('"', ''))

class Clase():
	def __init__(self, clase):
		pass
		#proximo a implementar