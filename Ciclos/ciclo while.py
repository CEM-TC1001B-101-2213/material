
i = 0 # dónde inicia nuestro ciclo
while i <= 4: # condición de paro, marca el final del ciclo
    print(f"El valor de i es: {i}")
    i = i + 1 # paso

print("-------------------")

i = 10 # dónde inicia nuestro ciclo
while i >= 1: # condición de paro, marca el final del ciclo
    print(f"El valor de i es: {i}")
    i = i - 1 # paso

print("-------------------")

texto = "hola"
i = 0
while i < len(texto):
    print(f"El valor de i es: {texto[i]}")
    i = i + 1
    
print("-------------------")

lista = [1.5, 7, "hola", [4,7], False]
i = 0
while i < len(lista):
    print(f"El valor de i es: {lista[i]}")
    i = i + 1

print("-------------------")

# Ciclo indefinido
# No sé cuántas veces se va a repetir
continuar = "s"
while continuar != "n":
    continuar = input("¿Desea continuar s/n?: ")