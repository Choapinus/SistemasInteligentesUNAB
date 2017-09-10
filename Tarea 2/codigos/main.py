if __name__ == '__main__':

	from filters import install_req

	install_req()

	from click import progressbar
	from etiquetas_class import Vector
	from filters import get_etiquetas, only_alpha, get_words, cross_validation
		


	#etiquetas = get_etiquetas(_csv='data/nombre.csv', _dat='data/nombre.dat') #para el que quiera editar

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
	print 'vectores guardados en la carpeta data'

	cross_validation()
	print 'cross-validation realizado en la carpeta /training'


	
	exit()
	

else:
	print 'c:'