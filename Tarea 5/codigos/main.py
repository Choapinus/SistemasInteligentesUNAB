import json
import threading
from TSP import TSP
from time import sleep
from Genetic import GeneticAlgorithm


def gen_thread1(tsp):
	gal = GeneticAlgorithm(tsp, max_pop = 5000, max_gen = 100000)

	for i in range(gal.max_generation): #100k
		gal.run()
		# print 'min fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))
	
	print 'min fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))
	print threading.currentThread().getName(), 'stoped'

	file = open('thread1.json', 'w')

	for obj in gal.actual_population:
		if obj.fitness == min(map(lambda x: x.fitness, gal.actual_population)):
			file.writelines(json.dumps(obj, default=lambda o: o.__dict__))
			break
	file.close()

def gen_thread2(tsp):
	gal = GeneticAlgorithm(tsp, max_pop = 10000, max_gen = 50000)

	for i in range(gal.max_generation):
		gal.run()
		# print 'min fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))
	
	print 'min fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))
	print threading.currentThread().getName(), 'stoped'

	file = open('thread2.json', 'w')

	for obj in gal.actual_population:
		if obj.fitness == min(map(lambda x: x.fitness, gal.actual_population)):
			file.writelines(json.dumps(obj, default=lambda o: o.__dict__))
			break
	file.close()


# tsp = TSP('../test/a280.tsp')  # con espacios al principio, 280 elementos
tsp = TSP('../test/Nueva Carpeta/att48.tsp')  # sin espacios al principio, 48 elementos
# tsp = TSP('../test/Nueva Carpeta/ch130.tsp')  # sin espacios al principio, 130 elementos

# print json.dumps(tsp, default=lambda o: o.__dict__) #best wea ever


# tsp = TSP('../test/Nueva Carpeta/mine.tsp')  # custom, 20 elements


t1 = threading.Thread(target=gen_thread1, args=(tsp,), name='gen_1')
t1.daemon = True

t2 = threading.Thread(target=gen_thread2, args=(tsp,), name='gen_2')
t2.daemon = True

t1.start()
t2.start()

cont = 0

while t1.isAlive() or t2.isAlive():
	sleep(10)
	cont += 1
	print str(cont)
	if t1.isAlive(): print t1.getName(), 'is runing'
	if t2.isAlive(): print t2.getName(), 'is runing\n'


#ahora son funciones distintas para cada thread
#verificar si con la mutacion mejora o no. Si fitness_actual < mutacion, desechar mutacion, else, mutar
#no se puede estimar cuanto se demora