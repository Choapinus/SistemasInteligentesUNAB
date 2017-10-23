;; funciones que retornan primer, segundo y tercer elemento de las listas
;; car -> retorna el primer elemento de una lista
;; cdr -> retorna el resto de la lista sin el primer elemento

(defun primer_elemento (lista)
	(car lista)
)

(defun segundo_elemento (lista)
	(car (cdr lista))
)

(defun tercer_elemento (lista)
	(car (cdr (cdr lista)))
)