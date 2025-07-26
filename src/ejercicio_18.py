"Mediante un ciclo while, genera y muestra la secuencia de Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000."

a, b = 1, 1

while a <= 1000:
    print(a)
    a, b = b, a + b
