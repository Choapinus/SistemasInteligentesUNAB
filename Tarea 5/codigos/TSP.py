class Node(object):
	"""
	Coordinates to represent axis X and Y of a node with a given id.
	Inherits from object (The most base type). Whitout it, Node cannot be inherited.
	"""
	def __init__(self, node_id, node_list):
		self.node_id = node_id
		self.x = node_list[0]
		self.y = node_list[1]

	def get_coords(self):
		"""
		Returns a tuple with the axis x and y
		"""
		return (self.x, self.y)

class TSP():
	""" 
	Parser of tsp file. 
	Only for edge_weight_type = EUC_2D and ATT

	seguir implementando mas edge_weight_type
	"""
	def __init__(self, file_name):
		file = open(file_name, 'r')
		data = file.readlines()
		file.close()

		self.name = data[0].split(':')[-1][1:].replace('\n','')
		self.comment = data[1].split(':')[-1][1:].replace('\n','')
		self.type = data[2].split(':')[-1][1:].replace('\n','')
		self.dimension = int(data[3].split(':')[-1])
		self.edge_weight_type = data[4].split(':')[-1][1:].replace('\n','')
		self.nodes = []

		if self.edge_weight_type.upper() not in ['EUC_2D', 'ATT']:
			raise TypeError(self.edge_weight_type+" not implemented. Exiting.")

		nodes_list = map(lambda x: x.replace('\n',''), data[6:-1])
		nodes_list = map(lambda x: x.split(), nodes_list) #nodes_list[0] = ['1', '6734', '1453'] //example

		for i in range(len(nodes_list)):
			del nodes_list[i][0]
		#nodes_list[0] = ['6734', '1453'] //example

		try:
			
			nodes_list = map(lambda x: map(lambda y: float(y), x), nodes_list)

			for i in range(1, self.dimension+1):
				self.nodes.append(Node(i, nodes_list[i-1]))

		except Exception as e:
			
			#print "Coordinate cannot been converted into float. Trying int instead."
			nodes_list = map(lambda x: map(lambda y: int(y), x), nodes_list)
			
			for i in range(1, self.dimension+1):
				self.nodes.append(Node(i, nodes_list[i-1]))