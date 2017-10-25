;; funcion que resuelve funcion cuadratica

(defun funcion_cuadratica (a b c)
	(setf solucion_1 (/ (+ (* -1.0 b) (sqrt (- (* b b) (* 4.0 a c)))) (* 2.0 a)))
	(setf solucion_2 (/ (- (* -1.0 b) (sqrt (- (* b b) (* 4.0 a c)))) (* 2.0 a)))
	(format t "x_1 = ~d, x_2 = ~d" solucion_1 solucion_2)
)