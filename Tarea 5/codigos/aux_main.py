if __name__ == '__main__':
	import json
	import click
	from TSP import TSP
	from Genetic import GeneticAlgorithm

	tsp = TSP('../test/Nueva Carpeta/att48.tsp')
	#tsp = TSP('../test/Nueva Carpeta/kroA200.tsp')


	# gal = GeneticAlgorithm(tsp, max_pop = 100, max_gen = 100, max_fit=350000.0, mut_rate=0.2)
	gal = GeneticAlgorithm(tsp, max_pop = 100, max_gen = 100, max_fit=150000.0, mut_rate=0.1)

	"""
	with click.progressbar(range(gal.max_generation)) as bar:
		for i in bar:
			gal.run()
	"""
	fit = -0.0
	for i in range(gal.max_generation):
		gal.run(fit)
		fit -= 500.0

	# print 'min fitness: ', min(map(lambda x: x.fitness, gal.actual_population))

	file = open('aux_main.json', 'w')

	#"""
	for obj in gal.actual_population:
		if obj.fitness == min(map(lambda x: x.fitness, gal.actual_population)):
			file.writelines(json.dumps(obj, default=lambda o: o.__dict__))
			break
	#"""

	file.close()

	print '\nbest fitness actual pop: ', min(map(lambda x: x.fitness, gal.actual_population))

	#Se demora 20 horas



else:
	print 'cc:'
