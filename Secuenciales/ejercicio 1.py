# Actividad 1
# Ejercicio 1
# Aram Baruch González Pérez - 965707
# Ana Laura - 852522

tipo_cambio = float(input("Indica el tipo de cambio: "))
precio_pesos =  float(input("Indica el precio del producto en pesos: "))

precio_dolares = precio_pesos / tipo_cambio

print(f"El precio del producto en dólares es: {precio_dolares:.2f}")