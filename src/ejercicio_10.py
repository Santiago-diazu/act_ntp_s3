
palabra = 0                                                  
while True:
    ingrese = input("Ingrese una palabra. Ingresa 'fin' si quieres finalizar. ")
    if ingrese == "fin":
        break
    palabra += 1
print("Total palabras ingrasadas:", palabra)