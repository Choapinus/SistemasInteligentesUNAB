from TSP import Node
from math import sqrt
from operator import sub, div, add
from random import random, randint


class Gen(Node):
	"""
	A Gen is basically used to represent a Chromosome
	It's only by convention
	"""

	def __init__(self, node):
		super(Gen, self).__init__(node.node_id, list(node.get_coords()))
		self.gen_id = node.node_id
		del self.node_id


class Chromosome(object):
	"""
	A Chromosome represents a possible solution (path)
	The path is a (collection) list of gens. 
	improtant: The head of the path will also be in the tail ( path.append(path[0]) )
	"""

	def __init__(self, list_of_gens, exp_fit=150000.0, dist_function=0, mutate_prob=0.2):
		"""
		list_of_gens must be a list of Gens objects.
		exp_fit is expected fitness. default = 30000.0
		For the fitness function:
			dist_function = 0 => euclidean dist (default)
			dist_function = 1 => manhattan dist
			dist_function = 2 => canberra dist
			dist_function = 3 => squared_cord // beware
			dist_function = 4 => squared_chi_squared
		mutate_prob is the given mutation probability. default = 0.5
		mutation_prob is the own probability to mute. Random float between [0, 1]

		"""
		self.path = list_of_gens
		self.path.append(self.path[0])  # head in the tail
		self.mutation_prob = random()
		self.expected_fitness = exp_fit
		# self.actually_fitness = float('inf')
		self.dist_func_id = dist_function
		self.dist_func = [self.euclidean, self.manhattan, self.canberra, self.squared_cord, self.squared_chi_squared]
		self.fitness = self.fitness_func()
		self.given_mutate_prob = mutate_prob
		self.can_mutate = self.mutation_prob < self.given_mutate_prob

	def mutation(self):
		"""
		Change path in a different way (kinda reversed).
		:return modified list of Gens
		"""
		if self.can_mutate:
			left_slice = self.path[1:len(self.path) / 2]
			right_slice = self.path[len(self.path) / 2: -1]
			left_slice.reverse()
			right_slice.reverse()
			self.path = [self.path[0]] + left_slice + right_slice + [self.path[-1]]
			self.fitness = self.fitness_func()

	def crossover(self, another_chromawesome, decreased_fit):
		"""
		Do a random crossover between chromosomes path to make a single new possible solution.
		Returns a new Chromosome (object)
		"""
		self_current_path = []  # gens ids => int
		chromawesome_current_path = []  # gens ids => int
		new_path = []  # new path with gen ids of old paths => int
		true_new_path = []  # gen_id to Gen objects

		# extract the paths of the chromosomes
		for i in range(len(self.path)):
			self_current_path.append(self.path[i].gen_id)
			chromawesome_current_path.append(another_chromawesome.path[i].gen_id)

		# define which will be the first node (and the last)
		if random() <= 0.5:
			new_path.append(self_current_path[0])
			self_current_path.remove(new_path[0])
			self_current_path.remove(new_path[0])
			try:
				# if both begins and ends with the same gen_id, it must be deleted
				chromawesome_current_path.remove(new_path[0])
				chromawesome_current_path.remove(chromawesome_current_path[-1])
				chromawesome_current_path.remove(new_path[0])
			except Exception:
				pass

		else:
			new_path.append(chromawesome_current_path[0])
			chromawesome_current_path.remove(new_path[0])
			chromawesome_current_path.remove(new_path[0])
			try:
				self_current_path.remove(new_path[0])
				self_current_path.remove(self_current_path[-1])
				self_current_path.remove(new_path[0])
			except Exception:
				pass

		# begin the crossover
		for i in range(len(self_current_path)):
			if random() >= 0.5:
				if self_current_path[i] not in new_path:
					new_path.append(self_current_path[i])
				elif chromawesome_current_path[i] not in new_path:
					new_path.append(chromawesome_current_path[i])
				else:
					aux_path = randint(1, len(self.path) - 1)
					while aux_path in new_path:
						aux_path = randint(1, len(self.path) - 1)
					new_path.append(aux_path)
			else:
				if chromawesome_current_path[i] not in new_path:
					new_path.append(chromawesome_current_path[i])
				elif self_current_path[i] not in new_path:
					new_path.append(self_current_path[i])
				else:
					aux_path = randint(1, len(self.path) - 1)
					while aux_path in new_path:
						aux_path = randint(1, len(self.path) - 1)
					new_path.append(aux_path)
		# new_path.append(new_path[0])  # head = tail
		# isn't necessary to clone the head into the tail. The Chromosome __init__() does it
		# end crossover

		# begin the transformation from gen_id to Gen objects
		for gen_id in new_path:
			for i in range(len(self.path)-1):
				if gen_id == self.path[i].gen_id:
					true_new_path.append(self.path[i])					
		# end of the transformation from gen_id to Gen objects

		return Chromosome(true_new_path, exp_fit=decreased_fit, dist_function=self.dist_func_id, mutate_prob=self.given_mutate_prob)

	def fitness_func(self):
		"""
		Fitness function of the Chromosome. It will return the summation of dists between
		the x position and the subsequent of it
		"""
		fit = 0.0
		for i in range(1, len(self.path)):
			fit += self.dist_func[self.dist_func_id](self.path[i - 1], self.path[i])
		return fit

	@staticmethod
	def euclidean(gen_1, gen_2):
		"""
		if p = (p1, p2,..., pn) and q = (q1, q2,..., qn) 
		d(p,q) = d(q,p) = sqrt((q1-p1)^2 + (q2-p2)^2 + ...)
		Returns the Euclidean dist between two Gens
		"""
		return sqrt(sum(map(lambda x: pow(x, 2), map(sub, gen_1.get_coords(), gen_2.get_coords()))))

	@staticmethod
	def manhattan(gen_1, gen_2):
		"""
		dist(x_i, x_j) = |(x_i1 - x_i2)| + ... + |(x_ir - x_ir)|
		Returns the Manhattan dist between two Gens
		"""
		return sum(map(abs, map(sub, gen_1.get_coords(), gen_2.get_coords())))

	@staticmethod
	def canberra(gen_1, gen_2):
		"""
		dist(x_i, x_j) = ( |(x_i1 - x_j1)| / x_i1 + x_j1 ) + ... + ( |(x_i - x_j)| / x_i + x_j )
		Returns the Manhattan dist between two Gens
		"""
		val1 = map(abs, map(sub, gen_1.get_coords(), gen_2.get_coords()))
		val2 = map(add, gen_1.get_coords(), gen_2.get_coords())
		return sum(map(div, val1, val2))

	@staticmethod
	def squared_cord(gen_1, gen_2):
		"""
		dist(x_i, x_j) = (sqrt(xi_1) - sqrt(xj_1))**2 + ... + (sqrt(xi_r) - sqrt(xj_r))**2
		Returns the Manhattan dist between two Gens
		"""
		try:
			ret_try = sum(map(lambda x: pow(x, 2), map(sub, map(sqrt, gen_1.get_coords()), map(sqrt, gen_2.get_coords()))))
			return ret_try
		except ValueError as val_e:
			#print(val_e)
			#print(" in squared_cord dist function. Returning Inf instead")
			return float('inf')

	@staticmethod
	def squared_chi_squared(gen_1, gen_2):
		"""
		dist(x_i, x_j) = ( (x_i1 - x_j1)**2 / x_i1 + x_j1 ) + ... + ( (x_ir - x_jr)**2 / x_ir + x_jr )
		Returns the Manhattan dist between two Gens
		"""
		val1 = map(lambda x: pow(x, 2), map(sub, gen_1.get_coords(), gen_2.get_coords()))
		val2 = map(add, gen_1.get_coords(), gen_2.get_coords())
		return sum(map(div, val1, val2))


class GeneticAlgorithm(object):
	"""
	Intended to be a genetic algorithm.
	The fitness function is the summation of all distances between the first node to the last node.
	There are at least 2 dist functions (manhattan and euclidean)
	Reassign max_pop to increase or decrease the population
	"""

	def __init__(self, _tsp, max_gen = 100, max_pop = 1000, max_fit=150000.0, mut_rate = 0.2):
		self.tsp = _tsp
		self.max_fitness = max_fit
		self.max_population = max_pop
		self.max_generation = max_gen
		self.mutation_rate = mut_rate
		self.last_generation = []
		# self.initial_population = self.generate_population()
		self.actual_population = self.generate_population(self.max_fitness)

	def generate_chromosomes(self, max_fit):
		"""
		Returns a Chromosome (collection of Gens) wich represents a path.
		:returns Gen list (Chromosome)
		"""
		gens = []
		indexes = []  # lista de indices de nodos utilizados
		for _ in range(self.tsp.dimension):
			ran = randint(0, self.tsp.dimension - 1)
			while ran in indexes:
				ran = randint(0, self.tsp.dimension - 1)
			gens.append(Gen(self.tsp.nodes[ran]))
			indexes.append(ran)
		return Chromosome(gens, exp_fit=max_fit, mutate_prob=self.mutation_rate)

	def generate_population(self, fit):
		"""
		Returns a list of Chromosomes which represents the population.
		:returns list of Chromosomes
		"""
		population = []  # lista de cromosomas
		for _ in range(self.max_population):
			population.append(self.generate_chromosomes(max_fit=fit))
		return population

	def run(self, decrease_fit):
		survivors = []
		new_gen = []
		self.last_generation = self.actual_population[:]
		popu = self.actual_population[:]

		# evaluate fitness and get the survivors
		for chromosome in popu:
			if chromosome.fitness <= chromosome.expected_fitness:
				survivors.append(chromosome)

		new_gen = survivors[:]

		# crossover
		for _ in range(len(popu) - len(survivors)):
			tryes = 0
			try:
				dad = survivors[randint(0, len(survivors) - 1)]  # chromosome dad
				mom = survivors[randint(0, len(survivors) - 1)]  # chromosome mom
				# new_gen.append(dad.crossover(mom))  # append a chromosome child
				child = dad.crossover(mom, decrease_fit)
				while child.fitness > dad.fitness or child.fitness > mom.fitness:
					# dad = survivors[randint(0, len(survivors) - 1)]  # chromosome dad
					# mom = survivors[randint(0, len(survivors) - 1)]  # chromosome mom
					# new_gen.append(dad.crossover(mom))  # append a chromosome child
					child = dad.crossover(mom, decrease_fit)
					tryes += 1
					if tryes >= 10000: # 10k tryes, dad and mom are not compatible to make a better child
						dad = survivors[randint(0, len(survivors) - 1)]  # chromosome dad
						mom = survivors[randint(0, len(survivors) - 1)]  # chromosome mom
						tryes = 0
				new_gen.append(child)
			except ValueError:
				print 'no survivors with the actual fitness: '+str(self.actual_population[0].fitness)
				pass

		self.actual_population = new_gen[:]

		# possible mutation in all survivors
		for i in range(len(survivors)):
			self.actual_population[i].mutation()

		min_fit = min(map(lambda x: x.fitness, self.actual_population))
		print 'min fitness actual pop: ', min_fit
