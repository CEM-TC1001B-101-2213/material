
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

print(lista)

# Agregar elemmentos al final de la lista
lista.append("hola")
print(lista)

lista1 = [4,6,"hola"]
lista2 = [8,2,True]

# Agrega todos los elementos de una lista a otra lista
lista1.extend(lista2)
print(lista1)

# lista.insert(índice, elemento)
# Agrega un elemento en el índice y recorre lo demás a la derecha
lista1.insert(3, "adios")
print(lista1)

# Elimina el primer elemento que coincide con el indicado
lista1.remove("hola")
print(lista1)

lista = [9,7,2,1,7,2,7,1]

# Invierte el orden de la lista
lista.reverse()
print(lista)

# Ordena de menor a mayor
lista.sort()
print(lista)

# Ordena de mayor a menor
lista.sort(reverse=True)
print(lista)