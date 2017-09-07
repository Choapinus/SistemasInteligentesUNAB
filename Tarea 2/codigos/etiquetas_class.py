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

class Vector():
	#1=undetermined, 2 = non-US, 3=world y 4=USA only.
	def __init__(self, clase, texto):
		lista_clases = ['Undetermined', 'Non-USA', 'World', 'USA only']
		self.clase = lista_clases.index(clase)+1
		self.palabras = set(texto.split())
		self.dict_palabras = {}
		self.dict_vector = {}
		self.vector = str(self.clase)
		
		for pal in self.palabras:
			self.dict_palabras[pal] = texto.count(pal)

	def make_vector(self, words_list):
		indices_palabras = []
		for palabra in self.dict_palabras.keys():
			if palabra in words_list:
				indices_palabras.append(words_list.index(palabra))
		for index in indices_palabras:
			self.dict_vector[index+1] = self.dict_palabras[words_list[index]]
		#construct the string
		keys = self.dict_vector.keys()
		keys.sort()
		for key in keys:
			self.vector += ' '+str(key)+':'+str(self.dict_vector[key])
		


