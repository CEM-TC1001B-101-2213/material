
udf1 = float(input("Proporciona tu calificación de la udf1: "))
udf2 = float(input("Proporciona tu calificación de la udf2: "))
udf3 = float(input("Proporciona tu calificación de la udf3: "))
udf4 = float(input("Proporciona tu calificación de la udf4: "))
udf5 = float(input("Proporciona tu calificación de la udf5: "))
udf6 = float(input("Proporciona tu calificación de la udf6: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6) / 6

# Esto es un comentario
# print(promedio)

# Formas para imprimir
print("El promedio de tu semestre fue de:", promedio, "Muy bien.")
print("El promedio de tu semestre fue de: " + str(promedio) + " Muy bien.")
print("El promedio de tu semestre fue de: {0:.2f} Muy bien.".format(promedio))
print(f"El promedio de tu semestre fue de: {promedio:.2f} Muy bien.")

