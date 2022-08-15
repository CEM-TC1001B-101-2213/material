# Actividad 1
# Ejercicio 2
# Aram Baruch González Pérez - 965707
# Ana Laura - 852522

parcial1 = float(input("Indica la calificación de tu parcial 1: "))
parcial2 = float(input("Indica la calificación de tu parcial 2: "))
proyecto = float(input("Indica la calificación de tu proyecto final: "))
examen = float(input("Indica la calificación de tu examen final: "))

calificacion = parcial1 * 0.2 + parcial2 * 0.35 + proyecto * 0.15 + examen * 0.3

print(f"La calificación final es: {calificacion:,.2f}")