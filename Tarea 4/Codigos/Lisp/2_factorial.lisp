;; funcion factorial

(defun factorial (num)
	(cond
		((= num 0) 1)
		(t
			(* num (factorial (- num 1)))
		)
	)
)