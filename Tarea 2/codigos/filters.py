import re, os, platform
from shutil import copyfile
from bs4 import BeautifulSoup
from etiquetas_class import Etiqueta, Perfil


def leer_csv(archivo_csv = 'data/Etiquetas-(a.valenzuelagonzlez@uandresbello.edu).csv', lista_textos_perfiles=None):
	arch = open(archivo_csv, 'r')
	data = arch.readlines()
	arch.close()
	del data[0] #data[0] => ['id_perfil;clase;lugares']

	etiquetas = {
	'USA only': [], 
	'Non-USA': [], 
	'World': [], 
	'Undetermined': []
	}

	#begin the clasification
	for element in data:
		if lista_textos_perfiles == None:
			obj = Etiqueta(element)
		else:
			#busqueda del id_perfil
			obj = Etiqueta(element)
			for perfil in lista_textos_perfiles:
				if obj.id_perfil == perfil.id_perfil:
					obj = Etiqueta(obj, perfil.texto, flag=True)

		etiquetas[obj.clase].append(obj)

	return etiquetas

def get_dat(archivo_csv='data/Perfiles-(a.valenzuelagonzlez@uandresbello.edu).dat'):
	perfiles = open(archivo_csv, 'r')
	perfiles = perfiles.readlines()

	#clean text from html tags
	for i in range(len(perfiles)):
		perfiles[i] = BeautifulSoup(perfiles[i], "html.parser").get_text()


	#lista de objetos Perfiles
	perfiles_texto = []
	for i in perfiles:
		perfiles_texto.append(Perfil(i))

	return perfiles_texto


def get_etiquetas(_csv=None, _dat=None):
	if _csv is None or _dat is None:
		return leer_csv(lista_textos_perfiles=get_dat())
	else:
		return leer_csv(_csv, lista_textos_perfiles=get_dat(_dat))


def get_stopwords(txt='data/stopwords.txt'):
	arch = open(txt, 'r')
	stopwords = arch.readlines()
	arch.close()

	for i in range(len(stopwords)):
		stopwords[i] = stopwords[i].replace('\n', '')

	return set(stopwords)

def only_alpha(etiquetas):
	regex = re.compile('[^a-zA-Z ]') #filtra todos los simbolos non-alpha, excepto los spaces
	for key in etiquetas.keys():
		for perfil in etiquetas[key]:
			perfil.texto = regex.sub('', perfil.texto)
			#string = regex.sub('', string) #ejemplo de uso
	return etiquetas

def get_words(etiquetas):
	words = set()
	stopwords = get_stopwords()
	for key in etiquetas.keys():
		for perfil in etiquetas[key]:
			for palabra in perfil.texto.split():
				words.add(palabra)
	
	words = words - stopwords

	return list(words)

def cross_validation(data='data/vectores.txt'):
	data = open(data, 'r')
	data = data.readlines()
	#Los S (splits del dataset)
	S_01 = open('training/S_train/S_01.dat', 'w')	
	S_02 = open('training/S_train/S_02.dat', 'w')
	S_03 = open('training/S_train/S_03.dat', 'w')
	S_04 = open('training/S_train/S_04.dat', 'w')
	S_05 = open('training/S_train/S_05.dat', 'w')
	S_06 = open('training/S_train/S_06.dat', 'w')
	S_07 = open('training/S_train/S_07.dat', 'w')
	S_08 = open('training/S_train/S_08.dat', 'w')
	S_09 = open('training/S_train/S_09.dat', 'w')
	S_10 = open('training/S_train/S_10.dat', 'w')

	for i in data[:200]:
		S_01.write(i)
	S_01.close()
	for i in data[201:400]:
		S_02.write(i)
	S_02.close()
	for i in data[401:600]:
		S_03.write(i)
	S_03.close()
	for i in data[601:800]:
		S_04.write(i)
	S_04.close()
	for i in data[801:1000]:
		S_05.write(i)
	S_05.close()
	for i in data[1001:1200]:
		S_06.write(i)
	S_06.close()
	for i in data[1201:1400]:
		S_07.write(i)
	S_07.close()
	for i in data[1401:1600]:
		S_08.write(i)
	S_08.close()
	for i in data[1601:1800]:
		S_09.write(i)
	S_09.close()
	for i in data[1801:2000]:
		S_10.write(i)
	S_10.close()

	#Los E (sets de entrenamiento)
	E_01 = open('training/E_train/E_01.dat', 'w')	
	E_02 = open('training/E_train/E_02.dat', 'w')
	E_03 = open('training/E_train/E_03.dat', 'w')
	E_04 = open('training/E_train/E_04.dat', 'w')
	E_05 = open('training/E_train/E_05.dat', 'w')
	E_06 = open('training/E_train/E_06.dat', 'w')
	E_07 = open('training/E_train/E_07.dat', 'w')
	E_08 = open('training/E_train/E_08.dat', 'w')
	E_09 = open('training/E_train/E_09.dat', 'w')
	E_10 = open('training/E_train/E_10.dat', 'w')


	for i in data[200:]:
		E_01.write(i)
	E_01.close()
	
	for i in data[:200]:
		E_02.write(i)
	for i in data[400:]:
		E_02.write(i)
	E_02.close()

	for i in data[:400]:
		E_03.write(i)
	for i in data[600:]:
		E_03.write(i)
	E_03.close()

	for i in data[:600]:
		E_04.write(i)
	for i in data[800:]:
		E_04.write(i)
	E_04.close()
	
	for i in data[:800]:
		E_05.write(i)
	for i in data[1000:]:
		E_05.write(i)
	E_05.close()
	
	for i in data[:1000]:
		E_06.write(i)
	for i in data[1200:]:
		E_06.write(i)
	E_06.close()
	
	for i in data[:1200]:
		E_07.write(i)
	for i in data[1400:]:
		E_07.write(i)
	E_07.close()
	
	for i in data[:1400]:
		E_08.write(i)
	for i in data[1600:]:
		E_08.write(i)
	E_08.close()
	
	for i in data[:1600]:
		E_09.write(i)
	for i in data[1800:]:
		E_09.write(i)
	E_09.close()
	
	for i in data[:1800]:
		E_10.write(i)
	E_10.close()



def install_req():
	if 'Win' in platform.system():
		
		if 'Python27' in os.getenv('PATH'):
			if os.system('python -m pip freeze | finstr "click"') == 1:
				os.system('python -m pip install click')

			if os.system('python -m pip freeze | findstr "bs4"') == 1:
				os.system('python -m pip install bs4')
			
			else:	
				print 'click module installed'

		else:
			if os.system('C:/Python27/python -m pip freeze | findstr "click"') == 1:
				os.system('C:/Python27/python -m pip install click')

			if os.system('C:/Python27/python -m pip freeze | findstr "bs4"') == 1:
				os.system('C:/Python27/python -m pip install bs4')

			else:
				print 'bs4 module installed'

	else:

		if os.system('python -m pip freeze | grep click') == 1:
			os.system('python -m pip install click')

		if os.system('python -m pip freeze | grep bs4') == 1:
			os.system('python -m pip install bs4')

		else:
			print 'bs4 module installed'


"""
listo: obtener todas las palabras de todos los perfiles, set y luego list para tener el "id"
listo: borrar stopwords
listo: despues, contar las palabras para cada vector
crear metodo que tome la lista de todas las palabras, que ubique el id de la llave del dict de las palabras de cada vector y genere el vector
"""


