longitud([],0).

longitud([_|L],N):-
	longitud(L,N1),N is N1 + 1.