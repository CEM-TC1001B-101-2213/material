
numero_personas = int(input("¿Cuántas personas serán encuestadas?: "))

i = 1
mayores_edad = 0
menores_edad = 0
empleados = 0
desempleados = 0
while i <= numero_personas:
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    empleo = int(input(f"Ingrese el estado laboral de la persona {i}: "))
    if edad >= 18:
        mayores_edad = mayores_edad + 1
    else:
        menores_edad = menores_edad + 1
    if empleo == 1:
        empleados = empleados + 1
    else:
        desempleados = desempleados + 1
    i = i + 1

print(f"Hay {mayores_edad} personas mayores de edad.")
print(f"Hay {menores_edad} personas menores de edad.")
print(f"Hay {empleados} personas empleadas.")
print(f"Hay {desempleados} personas desempleadas.")