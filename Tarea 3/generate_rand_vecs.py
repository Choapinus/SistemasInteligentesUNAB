from random import randint

arch = open('vectores.txt', 'r')
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