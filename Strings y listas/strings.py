
texto = "Hola"
print(texto)

texto = """Hola
¿cómo
estás?"""
print(texto)

texto = "Hola " * 3
print(texto)

texto = "Hola " + "mundo"
print(texto)

texto = "Hola mundo"

# Accediendo a una posición
print(texto[3])
print(texto[-4])

# Accediendo a un conjunto de caracteres
# [inicio:final] -> No toca el final
print(texto[3:6])

# [:final] -> Toma desde el inicio del texto y llega hasta antes del final
print(texto[:6])

# [inicio:] -> Toma desde mi punto de inicio y llega hasta el final del texto
print(texto[3:])

# [inicio:final:paso] -> Toma desde inicio hasta antes de final y va de paso en paso
print(texto[3:6:2])

print(texto[::-1])

# Secuencias de escape
texto = "Hola\nmundo"
print(texto)

texto = "\"Hola mundo\""
print(texto)

texto = "Hola mundo"
print(texto.upper())

print(texto.lower())

print(texto.title())

print(texto.replace("Hola", "Adios"))
print(texto.replace("o", "0"))

texto = "    Hola mundo    \t \n"
print(texto.strip())

lista = ["Hola", "mundo", "¿cómo", "estás?"]
print(" ".join(lista))
print(" -+- ".join(lista))

texto = "Hola mundo, ¿cómo estás?"
lista = texto.split()
print(lista)

lista = texto.split("o")
print(lista)

texto = "Hola mundo"
print(len(texto))

print(texto.count("o"))

print(texto.find("o"))

print(texto.index("o"))

print(texto.isalpha()) # Pregunta si existen puras letras
print(texto.isnumeric()) # Pregunta si existen puros números
print(texto.isalnum()) # Pregunta si existen sólo letras y números

print(texto.startswith("Ho"))
print(texto.endswith("do"))

numero = 2022
print(str(numero).endswith("22"))