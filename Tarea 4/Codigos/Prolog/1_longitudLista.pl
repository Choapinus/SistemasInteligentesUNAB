longitud_lista([], 0).

longitud_lista([_|L], N):-longitud_lista(L, N1), N is N1+1.