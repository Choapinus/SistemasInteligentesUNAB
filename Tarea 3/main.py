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

		if( len(cents[0]) > 1000 and len(cents[0]) < 200 and 
			len(cents[1]) > 1000 and len(cents[1]) < 200 and 
			len(cents[2]) > 1000 and len(cents[2]) < 200 and 
			len(cents[3]) > 1000 and len(cents[3]) < 200 and):
			main()



else:
	print 'c:'
