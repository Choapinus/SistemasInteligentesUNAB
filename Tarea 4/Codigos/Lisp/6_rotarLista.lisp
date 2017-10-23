(defun rotar_izquierda (lista)
	(append (cdr lista) (list (car lista)))
)