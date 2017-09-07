class Etiqueta():
	def __init__(self, perfil, texto=None, flag=False):
		if flag == False:
			perfil = perfil.split(';')
			self.id_perfil = perfil[0]
			self.clase = perfil[1]

			if ',' not in perfil[2]:
				self.lugares = perfil[2][:-1]
			else:
				lista_lugares = perfil[2].split(',')
				for i in range(len(lista_lugares)):
					while lista_lugares[i].startswith(' '):
						lista_lugares[i] = lista_lugares[i][1:]
					while lista_lugares[i].endswith(' '):
						lista_lugares[i] = lista_lugares[i][:-1]
					if lista_lugares[i].endswith('\n'):
						lista_lugares[i] = lista_lugares[i][:-1]
				self.lugares = lista_lugares
			self.texto = texto
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