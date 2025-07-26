suma = 0
while True:
    ingrese = input("Ingrese un número ")
    if ingrese == "0":
        break
    suma += float(ingrese)
print("Total:", suma)