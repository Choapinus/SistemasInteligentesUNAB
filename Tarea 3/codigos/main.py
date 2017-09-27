if __name__ == '__main__':

	from pymongo import MongoClient
	from util import Vector
	from pprint import pprint
	import time, os

	client = MongoClient() #localhost
	db = client['SI'] #get SI db
	vectores = db['vectores'] #get collection
	ret_vectors = [] #retrieved data

	while True:
		try:
			option = int(raw_input('\n0.- Salir\n1.- Insertar datos\n2.- Comprobar datos (primeros 5)\n3.- Recuperar datos\n4.- Eliminar datos\n\nopcion: '))
			
		except ValueError:
			print 'Opcion no valida, saliendo...'
			exit()
		except Exception as ex:
			print 'algo malio sal'
			print ex
			print 'saliendo...'
			exit()

		#options
		if option == 0:
			exit()

		elif option == 1:
			if vectores.count() == 0:
				if not os.path.exists('data/vectores.txt'):
					print 'Copie y pegue sus 2000 vectores en la carpeta data, yo le espero'
					time.sleep(3.5)
					print 'yamete kudasai onii-chan'
				
				else:
					arch = open('data/vectores.txt', 'r')
					data = arch.readlines()
					arch.close()

					#begin creation and insertion
					for vec_txt in data:
						vectores.insert_one(Vector(vec_txt).__dict__)
					
					del arch, data #release

					print 'data stored in mongodb!'
			else:
				print 'mongodb already contains data'

		elif option == 2:
			vec_cursor = vectores.find()
			
			try:
				for i in range(5):
					pprint(vec_cursor.next())
			
			except StopIteration:
				if vec_cursor.count() == 0:
					print 'No existen elementos para mostrar'
			
			del vec_cursor


		elif option == 3:
			if len(ret_vectors) == 0:
				vec_cursor = vectores.find()
				
				while vec_cursor.alive and vec_cursor.count() > 0:
					ret_vectors.append(Vector(vec_cursor.next()))
				
				if len(ret_vectors) > 0:
					print 'data stored in ram, use it wisely'
					pprint(ret_vectors[0].__dict__)
				
				else:
					print 'No existen elementos para mostrar'
			else:
				print 'data disposed already!!'

		elif option == 4:
			if vectores.count() > 0:
				vectores.drop()
				print 'deleted data'
			
			else:
				print 'no data to delete'

		else:
			print 'opcion no valida, reingrese'



			
		


else:
	print 'c:'





	

