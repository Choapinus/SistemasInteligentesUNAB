mayor(nil, 0).

mayor(t(I, R, D), M):- 
	mayor(I, MI),
 	mayor(D, MD), 
 	M1 is max(MI, MD), 
 	M is max(R, M1).