import math
import random

class SalesMan():
	def __init__(self):
		#valor de fitness, el camino total y la probablidad
		self.fitness = 0 
		self.path = list()
		self.probability = 0
	## 	Metodo que genera al azar el primer camino
	def randomFirstPath(self, townList):
		#lista de caminos visitados
		usedToGo = list()
		## mientras el camino de la lista no sean iguales 
		#se selecciona el siguiente pueblo, si no esta en la lista de pueblos ya visitados
		#se agrega a la lista del camino
		while (len(self.path) != len(townList)):
			nextTown = random.randint(1, 200)
			if nextTown not in usedToGo:
				self.path.append(nextTown)
				usedToGo.append(nextTown)
		#Metodo para seleccionar el punto de inicio al azar, 
		#el valor depende de la cantidad de ciudades que tenga el problema
	def randomStartingPoint(self):
		startingPoint = random.randint(1, 200)
		self.startingPoint = startingPoint
	#Calcula la distancia euclidiana entre dos puntos.
	def calculateDistanceBetweenPoint(self, x1, y1, x2, y2):
		distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1-y2), 2))
		return distance
	#SETTERS Y GETTERS
	def setPath(self, path):
		self.path = path

	def getPath(self):
		return self.path

	def calculateFitness(self, costMatrixDict, townList):
		self.fitness = 0
		pathIndex = 0
		while pathIndex <= len(townList) - 2:
			self.fitness = self.fitness + costMatrixDict[int(self.path[pathIndex])][int(self.path[pathIndex+1])]
			pathIndex = pathIndex + 1

	def setFitness(self, fitness):
		self.fitness = fitness

	def getFitness(self):
		return self.fitness

	def getProbability(self): 
		return self.probability

	def setProbability(self, probability):
		self.probability = probability
