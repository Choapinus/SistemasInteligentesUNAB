if __name__ == '__main__':
	from functions import generate_random_vectors, get_centroids, get_centroids_choppy, main
	from centroids import Centroid

	#opcion 1 es para calcular las weas de centroides hasta que den algo cercano a la realidad
	option = 1

	if option == 1:
		main()
	else:
		cents = []
		cents_data = get_centroids_choppy()
		
		for data in cents_data:
			if data != '\n':
				cents.append(Centroid(data))

		else:
			print 'cambie la opcion'

else:
	print 'c:'
