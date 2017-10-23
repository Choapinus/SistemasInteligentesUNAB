;; funcion que retorna el promedio del cuadrado de dos numeros
;; en el caso de querer promedio con coma flotante, poner un 2.0 en vez de un 2

(defun promedio_cuadrado (num1 num2)
	(/ (+ (* num1 num1) (* num2 num2)) 2)
)