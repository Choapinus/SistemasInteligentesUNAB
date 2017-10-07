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
	centroids = centroids.split('\n')
	del centroids[-1] #contiene nada y tira error por culpa de esta wea
	return centroids

def get_centroids_choppy(name='centroids_detail.txt'):
	arch = open(name, 'r')
	centroids = arch.readlines()
	arch.close()
	return centroids