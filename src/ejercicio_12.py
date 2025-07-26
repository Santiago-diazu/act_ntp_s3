"Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado."

i = int(input("Ingrese número entero: "))
factorial = 1

while i > 1:
    factorial *= i
    i -= 1

print("El factorial de", i, "es", factorial)

