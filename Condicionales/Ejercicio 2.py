
print("Bienvenid@ al programa de apoyos.")

edad = int(input("Indroduzca su edad: "))

if edad < 35:
    print("Lo sentimos, no tiene la edad requerida para calificar para un apoyo.")
elif edad <= 50:
    menores = int(input("¿Cuántos hijos menores de edad tienes?: "))
    mayores = int(input("¿Cuántos hijos mayores de edad tienes?: "))
    apoyos = 3000 + menores * 1000 + mayores * 500
    print(f"Usted tiene derecho a un apoyo de ${apoyos:,.2f} pesos.")
else:
    menores = int(input("¿Cuántos hijos menores de edad tienes?: "))
    mayores = int(input("¿Cuántos hijos mayores de edad tienes?: "))
    apoyos = 4500 + menores * 1000 + mayores * 500
    print(f"Usted tiene derecho a un apoyo de ${apoyos:,.2f} pesos.")
    
if edad < 35:
    print("Lo sentimos, no tiene la edad requerida para calificar para un apoyo.")
else:
    if edad < 50:
        apoyo_base = 3000
    else:
        apoyo_base = 4500
    menores = int(input("¿Cuántos hijos menores de edad tienes?: "))
    mayores = int(input("¿Cuántos hijos mayores de edad tienes?: "))
    apoyos = apoyo_base + menores * 1000 + mayores * 500
    print(f"Usted tiene derecho a un apoyo de ${apoyos:,.2f} pesos.")