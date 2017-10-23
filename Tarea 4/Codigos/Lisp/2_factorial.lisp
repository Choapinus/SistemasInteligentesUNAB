;; funcion factorial

(defun factorial (num)
	(cond
		((= num 1) 1)
		(t
			(* num (factorial (- num 1)))
		)
	)
)