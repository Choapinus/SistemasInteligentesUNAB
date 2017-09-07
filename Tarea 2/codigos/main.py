import os

if __name__ == '__main__':
	
	if 'Python27' in os.getenv('PATH'):
		if os.system('python -m pip freeze | grep click') == 1:
			os.system('python -m pip install click')
			print 'click module installed'
		from click import progressbar

		if os.system('python -m pip freeze | grep bs4') == 1:
			os.system('python -m pip install bs4')
			print 'bs4 module installed'
	else:
		if os.system('C:/Python27/python -m pip freeze | grep click') == 1:
			os.system('C:/Python27/python -m pip install click')
			print 'click module installed'
		from click import progressbar

		if os.system('C:/Python27/python -m pip freeze | grep bs4') == 1:
			os.system('C:/Python27/python -m pip install bs4')
			print 'bs4 module installed'

	from filters import get_etiquetas, only_alpha, get_words
	from etiquetas_class import Vector
		
	#etiquetas = get_etiquetas(_csv='nombre.csv', _dat='nombre.dat') #para el que quiera editar

	etiquetas = get_etiquetas() #se obtienen las etiquetas
	etiquetas = only_alpha(etiquetas) #se filtran los simbolos
	palabras = get_words(etiquetas) #lista de palabras sin repetir y sin stopwords

	print '\nPalabras contadas:', len(palabras)
	print

	vectores = []

	for key in etiquetas.keys():
		for perfil in etiquetas[key]:
			vectores.append(Vector(key, perfil.texto))

	print 'making vectors!!'
	with progressbar(vectores) as bar:
		for vector in bar:
			vector.make_vector(palabras)

	#save
	arch = open('data/vectores.txt', 'w')
	for vector in vectores:
		arch.write(vector.vector)
		arch.write('\n')
	arch.close()
	print 'vectores guardados en la carpeta data, bai~'

	
	exit()
	

else:
	print 'c:'