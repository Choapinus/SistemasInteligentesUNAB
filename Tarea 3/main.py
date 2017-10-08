if __name__ == '__main__':
	from functions import generate_random_vectors, get_centroids, get_centroids_choppy, main
	from centroids import Centroid

	#opcion 1 es para calcular las weas de centroides hasta que den algo cercano a la realidad
	option = 2

	if option == 1:
		main()
	else:
		cents = []
		cents_data = get_centroids_choppy()
		
		for data in cents_data:
			if data != '\n':
				cents.append(Centroid(data))

		for i in range(len(cents)):
			print 'centroid: ', cents[i].name
			print 'length data: ', cents[i].data.__len__()
			print 'data: ', cents[i].etiquetas
			print '\nmetrics:\n\t   ################'
			for j in range(len(cents[i].metrics)):
				print '\n\tname: ', cents[i].metrics[j].name
				print '\tentropy: ', cents[i].metrics[j].entropy
				print '\tpurity: ', cents[i].metrics[j].purity
				print '\tprecision: ', cents[i].metrics[j].precision
				print '\trecall: ', cents[i].metrics[j].recall
				print '\tF1 - Score: ', cents[i].metrics[j].f1_score
				print 
			print '\t   ################'
			print
		

else:
	print 'c:'