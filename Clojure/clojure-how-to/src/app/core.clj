(ns app.core)

;; scalar values
(println true)
(println false)
(println nil)

;; basics
(def x 42)
(println x)

;(def my-str "hi")
;(println my-str)

;; some numbers
(+ 1 1)
(+ 1
   (* 2 3)
   (/ 10 2))

;; data structures
[1 2 3]                                           ;; vector
[1 :two "three"]                                  ;; vector
{:a 1 :b 2}                                       ;; hash map
#{1 2 1 "b" true}                                 ;; set

;; defining functions
(defn square [num] (* num num))
(square 4)
(map square [1 2 3])
(reduce + (map square [1 2 3]))

;; multiple arguments
(defn do-things
  ([x]
   (println "I do" x))
  ([x y]
   (println "I do" x "and" y))
  ([x y z]
   (println "I do" x "," y "and" z)))
(do-things "sleeping")
(do-things "sleeping" "dreaming")
(do-things "sleeping" "dreaming" "eating")

; higher order functions
(map inc [1 2 3 4 5])                                       ;; map
(filter even? (range 10))                                   ;; filter
(reduce + (filter even? (range 10)))                        ;; reduce