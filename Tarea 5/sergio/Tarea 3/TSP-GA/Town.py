class Town:
	def __init__(self, townNumber, x, y):
		self.townNumber = townNumber
		self.x = x
		self.y = y

	def getTownNumber(self):
		return self.townNumber

	def getX(self):
		return self.x

	def getY(self):
		return self.y
#Objeto town que tiene las cordenadas y el numero de ciudad, sus getters como metodos