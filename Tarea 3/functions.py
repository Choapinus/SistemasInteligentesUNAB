from random import randint
from subprocess import check_output

def generate_random_vectors(name='vectores.txt'):
	"""
	Cada vez que se ocupe esta funcion, el modelo y los centroides variaran
	debido a que el orden de llegada de los vectores al yakmo afecta todo
	"""
	arch = open(name, 'r')
	vecs = arch.readlines()
	arch.close()

	rand = randint(0,1999)
	indices = []

	while indices.__len__() < 2000:
		if rand not in indices:
			indices.append(rand)
		else:
			rand = randint(0,1999)


	rand_vec = open('rand_vec.txt', 'w')

	for i in indices:
		rand_vec.write(vecs[i])
	rand_vec.close()
	print 'archivo rand_vec.txt creado'

def get_centroids(name='rand_vec.txt'):
	centroids = check_output(('yakmo -k 4 '+name+' - - -O 1').split())
	arch = open('centroids_detail.txt', 'w')
	arch.writelines(centroids)
	arch.close()
	centroids = centroids.split('\n')
	del centroids[-1] #contiene nada y tira error por culpa de esta wea
	return centroids

def get_centroids_choppy(name='centroids_detail.txt'):
	arch = open(name, 'r')
	centroids = arch.readlines()
	arch.close()
	return centroids

def main(vectores_original='vectores.txt', random_vectores='rand_vec.txt'):
	cents = []

	generate_random_vectors(vectores_original) #descomentar para quien no tenga sus vectores random creados
	cents_data = get_centroids(random_vectores)
	
	for data in cents_data:
		cents.append(Centroid(data))

	if( len(cents[0].data) > 1300 or len(cents[0].data) < 150 or 
		len(cents[1].data) > 1300 or len(cents[1].data) < 150 or 
		len(cents[2].data) > 1300 or len(cents[2].data) < 150 or 
		len(cents[3].data) > 1300 or len(cents[3].data) < 150):
		main()
	else:
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