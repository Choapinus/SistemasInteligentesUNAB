pertenece([X|_], X).

pertenece([_|L], X):- pertenece(L, X).