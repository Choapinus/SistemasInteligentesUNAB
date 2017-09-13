def getKey(item):
    return float(item[1])

vectors = open('test09.txt','r+')
pred = open('Predi09F.txt','r+')
mmr= open('mmr09F.txt','w')

totalMMR=0
reales=[]
#guardar los valores reales de data
for line in vectors:
    print line[0]
    r = line[0]
    reales.append(r)
    
aux = []
Saux = []
i=0
it=0
cont= 0
#leer de predicciones y calcular mmr
for line2 in pred:
    line2 = line2.split()
    aux = list(enumerate(line2))
    aux = aux[1:]
    Saux = sorted(aux, key=getKey,reverse = True)
    if reales[it]==line2[0]:
        totalMMR += 1
	cont+=1
	wformat = str(cont)+' MMR :'+str(1)+"\n"
	mmr.write(wformat)        
        print "son iguales"
    else:
        for x,y in Saux:
            if str(x)==reales[it]:
                i+=1
                totalMMR += round(1.0/i,3)
		cont+=1
		wformat = str(cont)+' MMR :'+str(round(1.0/i,3))+"\n"
		mmr.write(wformat) 		
                break
            else:
                i+=1 
                print "no son iguales"
            
    it+=1
    i=0
    
final = "Total MMR = "+str(totalMMR)+"/65  = "+str(totalMMR/65.0)
mmr.write(final)





print totalMMR



vectors.close()
pred.close()
mmr.close()