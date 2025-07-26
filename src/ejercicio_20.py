"Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado."

print("Ingrese una edad. Escribe -1 para terminar.")

mayorEdad = None

while True:
    try:
        edad = int(input("Edad: "))
        if edad == -1:
            break
        if mayorEdad is None or edad > mayorEdad:
            mayorEdad = edad
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

if mayorEdad is not None:
    print(f"La edad mayor ingresada fue: {mayorEdad}")
else:
    print("No se ingresaron edades válidas.")
