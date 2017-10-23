(defun factorial (N)
	(cond ( (zerop N) 1)
		(t ( 
			* N (factorial (- N 1)))
		)
	)

)
  