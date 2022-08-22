
numero = int(input("Indica el número hasta el que quieres sumar: "))

suma = 0
for i in range(numero+1):
    suma = suma + i

print(f"El valor de la suma desde 1 hasta {numero} es: {suma}")

suma = 0
i = 0
while i <= numero:
    # suma = suma + i
    suma += i # Abreviación
    #i = i + 1
    i += 1

print(f"El valor de la suma desde 1 hasta {numero} es: {suma}")