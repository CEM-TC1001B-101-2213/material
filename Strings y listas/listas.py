
lista = [1, 2, "hola"]
print(lista)

lista = [1, 2] * 3
print(lista)

lista = [1, 2] + [7, 8]
print(lista)

lista = [1, 5.7, [7,8], "hola", True]

print(lista[4])
print(lista[-1])

print(lista[2:4])
print(lista[:4])
print(lista[2:])
print(lista[::-1])

# Posiciones inician en 0
lista = [1,5,8,2,7,1,9,1]

print(len(lista))

print(sum(lista))

print(max(lista))
print(min(lista))

promedio = sum(lista) / len(lista)
print(promedio)

elemento = lista.pop(3)
print(elemento)
print(lista)

lista2 = lista.copy()

print(lista.index(8))
print(lista.count(1))