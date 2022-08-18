sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 578.52:
    limite_inferior = 0.01
    porcentaje = 0.0192
    cuota = 0
elif sueldo <= 4910.18:
    limite_inferior = 578.53
    porcentaje = 0.064
    cuota = 11.11
elif sueldo <= 8629.2:
    limite_inferior = 4910.19
    porcentaje = 0.1088
    cuota = 288.33

isr = (sueldo - limite_inferior) * porcentaje + cuota