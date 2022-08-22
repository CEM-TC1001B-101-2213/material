
numero_udfs = int(input("Indica cuántas udfs cursaste: "))

promedio = 0 # acumulador
for i in range(1, numero_udfs+1):
    udf = float(input(f"Proporciona tu calificación de la udf{i}: "))
    promedio = promedio + udf
promedio = promedio / numero_udfs

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