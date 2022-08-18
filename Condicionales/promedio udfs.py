
udf1 = float(input("Proporciona tu calificación de la udf1: "))
udf2 = float(input("Proporciona tu calificación de la udf2: "))
udf3 = float(input("Proporciona tu calificación de la udf3: "))
udf4 = float(input("Proporciona tu calificación de la udf4: "))
udf5 = float(input("Proporciona tu calificación de la udf5: "))
udf6 = float(input("Proporciona tu calificación de la udf6: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6) / 6

print(f"El promedio de tu semestre fue de: {promedio:.2f}.")

# Más de 90 - Excelente
# 80 y 90 - Bueno
# Para los demás - Falta estudiar más

if promedio > 90:
    print("Fue un excelente semestre.")
elif promedio >= 80:
    print("Fue un buen semestre.")
else:
    print("Te hace falta estudiar más.")