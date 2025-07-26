"Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final."

import random

aleatorio = random.randint(1, 10)
intento = 0

while intento != aleatorio:
    try:
        intento = int(input("Ingresa un número del 1 al 10: "))
        if intento != aleatorio:
            print("El número ingresado es diferente al generado aleatoriamente.")
    except ValueError:
        print("Ingrese un número válido.")

print(f"Has adivinado el número secreto: {aleatorio}")
