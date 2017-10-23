(defun izquierda (L)
	(append 
		(cdr L) (list 
					(car L)
				)
	)	
)
