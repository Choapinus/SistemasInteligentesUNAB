(defun cuadra (A B C)
	(setq x1 ( / (+ (* -1 B) (sqrt (- (* B B) (* 4 A C))))  (* 2 A)))
	(setq x2 ( / (- (* -1 B) (sqrt (- (* B B) (* 4 A C))))  (* 2 A)))
	(format t "x1 = ~2d x2 = ~2d" x1 x2)

)