if __name__ == '__main__':

	from os import listdir
	from vector import Vector

	s_train = listdir('S_train/') #lista de archivos en S_train.dat
	predictions = listdir('predictions/') #lista de archivos predictions.dat

	for i in range(len(s_train)):
		s_train[i] = 'S_train/'+s_train[i]
		s_train[i] = open(s_train[i], 'r')
		s_train[i] = s_train[i].readlines()

	for i in range(len(predictions)):
		predictions[i] = 'predictions/'+predictions[i]
		predictions[i] = open(predictions[i], 'r')
		predictions[i] = predictions[i].readlines()

	#print 's_train:', s_train[0][0]
	#print 'predictions', predictions[0][0]

	vectores = []
	mrr = 0.0

	for i in range(len(s_train)):
		vectores.append(Vector(s_train[i], predictions[i]))

	for i in range(len(vectores)):
		print 'iteracion '+str(i+1)
		print 'aciertos: '+str(vectores[i].correctos)
		print 'errores: '+str(vectores[i].incorrectos)
		print 'mrr: '+str(vectores[i].mrr/200.0)
		mrr += vectores[i].mrr
		print 'average loss: '+str(float(vectores[i].incorrectos)/200.0*100.0) #200 por ser de 200 elementos los splits
		print 'accuracy: '+str(vectores[i].correctos/200.0)
		print 'cant de non-usa: '+str(vectores[i].ocurrencias['Non-USA'])
		print 'cant de undet: '+str(vectores[i].ocurrencias['Undetermined'])
		print 'cant de world: '+str(vectores[i].ocurrencias['World'])
		print 'cant de usa only: '+str(vectores[i].ocurrencias['USA only'])
		print
	print 'mrr general: '+str(mrr/2000.0)


	print
	print 'para la curva roc'

	usa_only = 0
	non_usa = 0
	undet = 0
	world = 0

	for vec in vectores:
		usa_only += vec.ocurrencias['USA only']
		non_usa += vec.ocurrencias['Non-USA']
		undet += vec.ocurrencias['Undetermined']
		world += vec.ocurrencias['World']
	print 'usa_only: '+str(usa_only)
	print 'non_usa: '+str(non_usa)
	print 'under: '+str(undet)
	print 'world: '+str(world)

	
	"""
	* corregir y calcular mrr (mrr) es por clase??

	* contar cuantas ocurrencias hubieron de cada etiqueta en las predicciones
	* Por convencion, la clase que uno le interesa identificar es la positiva, y todo el resto se le llama negativo.
	* Accuracy: El ratio de casos correctamente clasificados versus el numero total de casos de prueba.

	Cuando se tengan los diez archivos de resultados, se debe calcular el
	desempeno del clasificador SVM para predecir la ubicacion geografica. Calcule
	el MRR y la matriz de confusion. Entregue tambien los promedios de los diez
	splits. Comente acerca de los errores. Hay algun patron?, Como podria
	mejorar?, Que puede decir de los errores?, Con respecto a las ubicaciones
	geograficas (strings) nota algun patron en los errores?
	Calcule la curva ROC, Lift, F(1)-score y el estimador AUC asumiendo cada una
	de las variables como positivas.


	done:
	* accuracy-desempeno
	
	"""
	



else:
	print 'c:'