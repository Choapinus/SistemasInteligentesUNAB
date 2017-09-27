class Vector():
	def __init__(self, vec):
		if type(vec) != dict:
			vec = vec.split()
			self.id_clase = int(vec[0])
			self.vector = ' '.join(vec[1:])
		else:
			self.id_clase = vec['id_clase']
			self.vector = vec['vector']




def install_req():
	import os, platform

	if 'Win' in platform.system():
		if 'Python27' in os.getenv('PATH'):
			if os.system('python -m pip freeze | finstr "mongo"') == 1:
				os.system('python -m pip install pymongo')
			
			else:	
				print 'mongo module installed'

		else:
			if os.system('C:/Python27/python -m pip freeze | findstr "mongo"') == 1:
				os.system('C:/Python27/python -m pip install pymongo')

			else:
				print 'mongo module installed'


	else:

		if os.system('python -m pip freeze | finstr "mongo"') == 1:
			os.system('python -m pip install pymongo')

		else:	
			print 'mongo module installed'
