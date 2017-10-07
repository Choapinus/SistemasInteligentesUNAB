if __name__ == '__main__':
	from functions import generate_random_vectors, get_centroids, get_centroids_choppy
	from centroids import Centroid

	def main():
		cents = []

		generate_random_vectors('vectores.txt') #descomentar para quien no tenga sus vectores random creados
		cents_data = get_centroids('rand_vec.txt')

		#cents_data = get_centroids_choppy('centroids_detail.txt')
		
		for data in cents_data:
			cents.append(Centroid(data))

		

		if(not (len(cents[0].data) > 1000 or len(cents[0].data) < 200 or 
			len(cents[1].data) > 1000 or len(cents[1].data) < 200 or 
			len(cents[2].data) > 1000 or len(cents[2].data) < 200 or 
			len(cents[3].data) > 1000 or len(cents[3].data) < 200 or)):
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
			main()



else:
	print 'c:'
