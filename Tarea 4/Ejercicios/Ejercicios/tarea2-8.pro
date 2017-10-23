maximo(nil,0).

maximo(t(I,R,D),M):-
	maximo(I,MI),
	maximo(D,MD),
	M1 is max(MI,MD),
	M is max(R,M1).