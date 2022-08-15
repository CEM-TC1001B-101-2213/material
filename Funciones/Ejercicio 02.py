
def bodymass(peso_kg, altura_m):
    bmi = peso_kg / altura_m ** 2
    return bmi

peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu estatura en metros: "))
resultado = bodymass(peso_kg, altura_m)
print(f"Tu BMI es: {resultado:,.2f}")