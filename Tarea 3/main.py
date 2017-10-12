if __name__ == '__main__':
	from functions import get_centroids_choppy, main
	from centroids import Centroid

	#opcion 1 es para calcular las weas de centroides hasta que den algo cercano a la realidad
	#opcion 2 es para ver los datos y metricas de manera entendible siempre y cuando se tengan los archivos necesarios
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
			total_entropy = 0.0
			total_purity = 0.0
			print 'centroid: ', cents[i].name
			print 'length data: ', cents[i].data.__len__()
			print '10 primeros: ', map(lambda x: int(x), cents[i].data[:10])
			print 'data: ', cents[i].etiquetas
			print '\nmetrics:\n\t   ################'
			for j in range(len(cents[i].metrics)):
				print '\n\tname: ', cents[i].metrics[j].name
				print '\tentropy: ', cents[i].metrics[j].entropy
				total_entropy += (float(sum(cents[i].etiquetas.values()))/2000.0)*cents[i].metrics[j].entropy
				print '\tpurity: ', cents[i].metrics[j].purity
				total_purity += (float(sum(cents[i].etiquetas.values()))/2000.0)*cents[i].metrics[j].purity
				print '\tprecision: ', cents[i].metrics[j].precision
				print '\trecall: ', cents[i].metrics[j].recall
				print '\tF1 - Score: ', cents[i].metrics[j].f1_score
				print '\n'
			print '\ttotal_entropy: ', total_entropy
			print '\ttotal_purity: ', total_purity
			print '\n\t   ################'
			print
		

else:
	print 'c:'