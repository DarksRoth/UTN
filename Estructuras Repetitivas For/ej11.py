numeroEntero = int(input("Ingrese un número: "))
esPrimo = True
cantPrimos = 0

for i in range(1, numeroEntero + 1):
    if i == 1:
        print(f"El número {i} no es primo")
    else:
        numero = i # numero = 3
        for j in range(2, numero): 
            if numero % j == 0:
                esPrimo = False
                break
        else:
            esPrimo = True
            cantPrimos += 1
        if esPrimo:
            print(f"El numero {i} es primo")
        else:
            print(f"El numero {i} no es primo")

print(f"La cantidad de números primos es: {cantPrimos}")
