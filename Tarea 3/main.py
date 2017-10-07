if __name__ == '__main__':
	from functions import generate_random_vectors, get_centroids, get_centroids_choppy, main
	from centroids import Centroid

	#opcion 1 es para calcular las weas de centroides hasta que den algo cercano a la realidad
	option = 2

	if option == 1:
		main()
	else:
		cents = []

		#generate_random_vectors('vectores.txt') #descomentar para quien no tenga sus vectores random creados
		#cents_data = get_centroids('rand_vec.txt')
		cents_data = get_centroids_choppy()
		
		for data in cents_data:
			if data != '\n':
				cents.append(Centroid(data))

		print cents[0].name
		print 'len data: ', cents[0].data.__len__()
		print cents[0].etiquetas
		print
		print cents[1].name
		print 'len data: ', cents[1].data.__len__()
		print cents[1].etiquetas
		print
		print cents[2].name
		print 'len data: ', cents[2].data.__len__()
		print cents[2].etiquetas
		print
		print cents[3].name
		print 'len data: ', cents[3].data.__len__()
		print cents[3].etiquetas
		print

else:
	print 'c:'