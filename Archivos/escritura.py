
archivo = open("ejemplo escritura.txt", "w", encoding="utf8")

archivo.write("Ejemplo\n")
archivo.write("Otro ejemplo")

#archivo.writelines(["Hola", "mundo"])

archivo.close()