"Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final."

numero = input("Ingrese un número entero positivo: ")

suma = 0
for digito in numero:
    suma += int(digito)

print(f"La suma de los dígitos de {numero} es: {suma}")
