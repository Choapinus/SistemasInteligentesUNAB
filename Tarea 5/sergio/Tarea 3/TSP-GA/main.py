from Town import Town
from costMatrix import CostMatrix
from salesMan import SalesMan
import random
import time 

#variables iniciales para el Genetic Algorithm
MAX_ITERATION = 100
MAX_POPULATION = 2000
PC = 0.8
PM = 0.05
#inicializa el cronometro
start_time = time.time()
#Crea una lista de objetos town
townList = list()
#Captura la info desde el archivo de texto
townData = open("town.txt", 'r')
while townData:
	line = townData.readline().split()
	if (line == []):
		break;
	townList.append(Town(line[0], line[1], line[2]))

#crear CostMatrix
costMatrixDict = CostMatrix(townList).createCostMatrix()

#crea la poblacion
populationList = list()
for i in range(20):
	populationList.append(SalesMan())
	populationList[i].randomFirstPath(townList)
	populationList[i].calculateFitness(costMatrixDict, townList)

#Comienza las iteraciones
iteration = 1
while iteration <= MAX_ITERATION:
	#ordena la lista populationList
	populationList = sorted(populationList, key=lambda population: population.fitness)
	#Calcula el fitness y la probabilidad
	sumFitness = 0
	for population in populationList:
		sumFitness = sumFitness + population.getFitness()
	probability = 0
	sumProbabilities = 0
	for population in populationList:
		population.setProbability(sumProbabilities + ((float(population.getFitness()) / float(sumFitness))))
		sumProbabilities += population.getProbability() - sumProbabilities
		population.setProbability(1 - population.getProbability())
	#fase de seleccion
	populationList = populationList[::-1]
	populationIndex = 0
	populationIndexSelectionList = list()
	#se va agregando a la populacion segun su probabilidad 
	while (len(populationIndexSelectionList) != MAX_POPULATION):
		randNumber = random.uniform(0, 1)
		for population in populationList:
			if randNumber < population.getProbability():
				populationIndexSelectionList.append(populationIndex)
				break
			populationIndex = populationIndex + 1
		populationIndex = 0
	populationSelectionList = list()
	#agrega las poblacion
	for i in range(MAX_POPULATION):
		populationSelectionList.append(populationList[populationIndexSelectionList[i]])

	#fase crossover
	crossoverCount = 0
	while crossoverCount < (MAX_POPULATION):
		parent1 = populationSelectionList[crossoverCount]
		parent2 = populationSelectionList[crossoverCount+1]
		#ocurre el crossover segun el parametro
		if random.uniform(0, 1) < PC:
			child1 = SalesMan()
			child2 = SalesMan()
			#Se genera la info del hijo 1
			child1.setPath(parent1.getPath()[:100])
			while len(child1.getPath()) != len(townList):
				parent2Path = parent2.getPath()
				for town in parent2Path:
					if town not in child1.getPath():
						child1.getPath().append(town)
			#se genera la del hijo 2
			child2.setPath(parent2.getPath()[:100])
			while len(child2.getPath()) != len(townList):
				parent1Path = parent1.getPath()
				for town in parent1Path:
					if town not in child2.getPath():
						child2.getPath().append(town)
			#se agregan a la poblacion
			populationList.append(child1)
			populationList.append(child2)
		#Si no ocurre crossover se copia el hijo al padre
		else:
			child1 = SalesMan()
			child2 = SalesMan()
			child1.setPath(parent1.getPath())
			child1.setFitness(parent1.getFitness())
			child2.setPath(parent2.getPath())
			child2.setFitness(parent2.getFitness())
			populationList.append(child1)
			populationList.append(child2)
		crossoverCount = crossoverCount + 2
	#Se calcula el fitness del hijo uno
	child1.calculateFitness(costMatrixDict, townList)

	calculateFitnessCount = 20
	while calculateFitnessCount < len(populationList):
		populationList[calculateFitnessCount].calculateFitness(costMatrixDict, townList)
		calculateFitnessCount = calculateFitnessCount + 1
	mutationIndex = 0
	#Elige los mejores segun la mutacion para agregarlos al camino desde la poblacion 
	for population in populationList:
		if mutationIndex >= 20:
			pathIndex = 0
			pathIndexList = list()
			for path in population.getPath():
				if random.uniform(0, 1) < PM:
					pathIndexList.append(pathIndex)
					if len(pathIndexList) == 2:
						temp = population.getPath()[pathIndexList[0]]
						population.getPath()[pathIndexList[0]] = population.getPath()[pathIndexList[1]]
						population.getPath()[pathIndexList[1]] = temp
						pathIndexList = list()
				pathIndex = pathIndex + 1
		mutationIndex = mutationIndex + 1
	#Ordena la lista de la poblacion
	populationList = sorted(populationList, key=lambda population: population.fitness)
	#elimina las poblacion de la lista para volver a realizar el proceso
	delIndex = 20
	while delIndex < len(populationList):
		del populationList[delIndex]
	iteration = iteration + 1 
#imprime la informacion 
print populationList[0].getPath()
print "Total distance: " + str(populationList[0].getFitness())
print "Runtime: ", time.time() - start_time
