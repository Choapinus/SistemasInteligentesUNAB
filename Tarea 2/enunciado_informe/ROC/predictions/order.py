a = open('prediction_all.csv', 'r')
c = a.readlines()
a.close()



for i in range(len(c)):
	c[i] = c[i].split(';')
	c[i][-1] = c[i][-1][:-2]
	c[i] = map(lambda x: float(x), c[i])
	c[i][0] = int(c[i][0])
	aux = c[i][0]
	del c[i][0]
	c[i].sort(reverse=True)
	c[i].insert(0, aux)

a = open('prediction_all_ordered.csv', 'w')

for i in range(len(c)):
	c[i] = map(lambda x: str(x), c[i])
	a.write(c[i][0]+';'+c[i][1]+';'+c[i][2]+';'+c[i][3]+';'+c[i][4]+'\n')