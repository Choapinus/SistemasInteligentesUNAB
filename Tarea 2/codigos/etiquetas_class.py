class Etiqueta():
	def __init__(self, perfil, texto=None, flag=False):
		if flag == False:
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
				self.texto = texto
				while self.lugares[0].startswith(' '):
					self.lugares[0] = self.lugares[0][1:]
				while self.lugares[0].endswith(' '):
					self.lugares[0] = self.lugares[0][:-1]
				for iterator in perfil:
					if type(iterator) != list:
						while iterator.startswith(' '):
							iterator = iterator[1:]
						while iterator.endswith(' '):
							iterator = iterator[:-1]
						self.lugares.append(iterator.replace('"', ''))
		else:
			self.id_perfil = perfil.id_perfil
			self.clase = perfil.clase
			self.lugares = perfil.lugares
			self.texto = texto


class Perfil():
	def __init__(self, perfil):
		perfil = perfil.split('\t')
		self.id_perfil = perfil[0]
		self.texto = perfil[1]