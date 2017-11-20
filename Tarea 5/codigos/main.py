import json
import datetime
import threading
from TSP import TSP
from time import sleep
from Genetic import GeneticAlgorithm


def gen_thread1(tsp):
	gal = GeneticAlgorithm(tsp, max_pop = 1000, max_gen = 1000, max_fit=140000.0, mut_rate=0.25)
	fit = 0.0

	for i in range(gal.max_generation):
		print threading.currentThread().getName(), 'generation:', str(i)
		print 'max fitness actual generation:', i+1, str(max(map(lambda x: x.fitness, gal.actual_population)))
		print 'min fitness actual generation:', i+1, str(min(map(lambda x: x.fitness, gal.actual_population)))
		print 'fitness decrement', str(fit)
		print
		gal.run(fit)
		
		if fit > str(min(map(lambda x: x.fitness, gal.actual_population))):
			#fit += gal.max_population*2.0/gal.max_generation
			fit += 30.0
		else: fit += 0.1

	file = open('gen1.json', 'w')

	#"""
	for obj in gal.actual_population:
		if obj.fitness == min(map(lambda x: x.fitness, gal.actual_population)):
			file.writelines(json.dumps(obj, default=lambda o: o.__dict__))
			break
	#"""

	file.close()

	print '\nbest fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))

def gen_thread2(tsp):
	gal = GeneticAlgorithm(tsp, max_pop = 1000, max_gen = 1000, max_fit=140000.0, mut_rate=0.25)
	fit = 0.0

	for i in range(gal.max_generation):
		print threading.currentThread().getName(), 'generation:', str(i)
		print 'max fitness actual generation:', i+1, str(max(map(lambda x: x.fitness, gal.actual_population)))
		print 'min fitness actual generation:', i+1, str(min(map(lambda x: x.fitness, gal.actual_population)))
		print 'fitness decrement', str(fit)
		print
		gal.run(fit)
		
		if fit > str(min(map(lambda x: x.fitness, gal.actual_population))):
			#fit += gal.max_population*2.0/gal.max_generation
			fit += 40.0
		else: fit += 0.1

	file = open('gen2.json', 'w')

	#"""
	for obj in gal.actual_population:
		if obj.fitness == min(map(lambda x: x.fitness, gal.actual_population)):
			file.writelines(json.dumps(obj, default=lambda o: o.__dict__))
			break
	#"""

	file.close()

	print '\nbest fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))


# tsp = TSP('../test/a280.tsp')  # con espacios al principio, 280 elementos
tsp = TSP('../test/Nueva Carpeta/att48.tsp')  # sin espacios al principio, 48 elementos
# tsp = TSP('../test/Nueva Carpeta/ch130.tsp')  # sin espacios al principio, 130 elementos

# print json.dumps(tsp, default=lambda o: o.__dict__) #best wea ever


# tsp = TSP('../test/Nueva Carpeta/mine.tsp')  # custom, 20 elements


#t1 = threading.Thread(target=gen_thread1, args=(tsp,), name='gen_1')
#t1.daemon = True

t2 = threading.Thread(target=gen_thread2, args=(tsp,), name='gen_2')
t2.daemon = True

t_init = datetime.datetime.now()

#t1.start()
t2.start()

#while t1.isAlive() or t2.isAlive():
while t2.isAlive():
	#if t1.isAlive(): print t1.getName(), 'is runing'
	#if t2.isAlive(): print t2.getName(), 'is runing\n'
	pass

t_end = datetime.datetime.now()

print(t_end-t_init)


#ahora son funciones distintas para cada thread