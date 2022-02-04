; Team OdinRachel Xiao, Yuqing Wu
; SoftDev
; K27 -- Where Does JS Live?
; 2022-02-04
; time spent: 0.5 hours

; Factorial
; The function nis a procedure (lambda) that takes in a parameter n
; If n is less than or equal to 1, the function should return 1
; If not, the function should return the value of n times the factorial of the preceding number
(define fact
  (lambda (n)
    (if (<= n 1)
        1
        (* n (fact (- n 1)))
        )
    )
  )
(fact 0)
(fact 1)
(fact 2)
(fact 3)
(fact 5)
(fact 10)

; Fibonacci sequence
; Each number in the sequence is the sum of the two preceding ones with the first two numbers being 0 and 1
(define fib
  (lambda (n)
         (if (<= n 1)
             n
             (+ (fib (- n 1))
                (fib (- n 2))
                )
             )
         )
  )

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)
(fib 10)