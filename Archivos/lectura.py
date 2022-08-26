
archivo = open("ejemplo.txt", "r", encoding="utf8")

# Lee todo el contenido del archivo y lo obtiene como un string
# texto = archivo.read()
# print(texto)

# readline() lee la siguiente línea de su archivo
# linea1 = archivo.readline()
# linea2 = archivo.readline()
# print(linea1)
# print(linea2)

# Lee el archivo y lo separa en líneas en una lista
# lineas = archivo.readlines()
# print(lineas)

for i in archivo:
    print(i)

archivo.close()