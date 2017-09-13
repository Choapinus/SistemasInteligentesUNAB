if __name__ == '__main__':

	from os import listdir

	s_train = listdir('../make_vectors/training/S_train/') #lista de S_train.dat
	predictions = listdir('../../svm_multiclass_windows/predictions/') #lista de predictions.dat

	for i in range(len(s_train)):
		s_train[i] = '../make_vectors/training/S_train/'+s_train[i]
		s_train[i] = open(s_train[i], 'r')
		s_train[i] = s_train[i].readlines()

	for i in range(len(predictions)):
		predictions[i] = '../../svm_multiclass_windows/predictions/'+predictions[i]
		predictions[i] = open(predictions[i], 'r')
		predictions[i] = predictions[i].readlines()

	print 's_train:', s_train[0][0]
	print 'predictions', predictions[0][0]

	vectores = []

	#hacer vectores y ver que wea pasa con los TP y los TN


	"""
	idea: verificar set_0x con su prediccion_0x
	calcular mmr
	"""



else:
	print 'c:'