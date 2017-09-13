;Tarea 2 LISP por Gustavo Veliz
;En este archivo estaran los 6 ejercicios pedidos para LISP

;FUNCION CUADRADO, ESTA FUNCION SE USARA PARA EL EJERCICIO d
(defun cuadrado (n)
(* n n))


;a) FUNCION CUBO, RECIBE UN VALOR N Y RETORNA SU VALOR AL CUBO
(defun cubo (n)
(* n(* n n)))

;b) FUNCION FACTORIAL, RECIBE UN VALOR N Y RETORNA SU VALOR FACTORIAL
(defun factorial (n)
(cond ((= n 1) 1)
(T (* n (factorial (- n 1)))) ))

;c) TRES FUNCIONES QUE RETORNEN EL PRIMER, SEGUNDO Y TERCER ELEMENTO DE UNA LISTA 
;c.1) Primer Elemento
(defun elemento1 (L)
(car L))

;c.2) Segundo Elemento 
(defun elemento2 (L)
(car (cdr L)))

;c.3) Tercer Elemento
(defun elemento3 (L)
(car (cdr (cdr L))))

;d) FUNCION QUE RETORNA EL PROMEDIO DEL CUADRADO DE DOS NUMEROS
(defun promcuadrados (L)
(/ (+ (cuadrado (elemento1 L)) (cuadrado (elemento2 L))) 2))

;e) FUNCION QUE CALCULE AX^2 + BX + C
(defun ABC (L)
(setq x1 (/ (+ (* -1 (elemento2 L)) (sqrt (+ (cuadrado (elemento2 L)) (* 4 (* (elemento1 L) (elemento3 L)))))) (* 2 (elemento1 L))))
(princ "X1")
(terpri)
(write x1)
(terpri)    
(terpri)
(princ "X2")
(setq X2 (/ (- (* -1 (elemento2 L)) (sqrt (+ (cuadrado (elemento2 L)) (* 4 (* (elemento1 L) (elemento3 L)))))) (* 2 (elemento1 L))))
)

;f) FUNCION QUE RECIBA UNA LISTA Y ROTE UN ELEMENTO HACIA LA IZQUIERDA
(defun rotarizquierda (L)
(append (cdr L) (LIST (car L))))

;(/ (+ (* -1 (elemento2 L)) (sqrt (+ (cuadrado (elemento2 L)) (* 4 (* (elemento1 L) (elemento3 L)))))) (* 2 (elemento1 L)))