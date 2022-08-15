
# Sin parámetros y sin valor de retorno
# def precio_a_dolares():
#     precio_pesos = float(input("Indica el precio en pesos: "))
#     tipo_cambio = float(input("Indica el tipo de cambio: "))
#     precio_dolares = precio_pesos / tipo_cambio
#     print(f"El precio en dólares es: ${precio_dolares:,.2f}")
    
# Sin parámetros y con valor de retorno
# def precio_a_dolares():
#     precio_pesos = float(input("Indica el precio en pesos: "))
#     tipo_cambio = float(input("Indica el tipo de cambio: "))
#     precio_dolares = precio_pesos / tipo_cambio
#     print(f"El precio en dólares es: ${precio_dolares:,.2f}")
#     return precio_dolares

# Con parámetros y con valor de retorno
def precio_a_dolares(precio_pesos, tipo_cambio):
    precio_dolares = precio_pesos / tipo_cambio
    print(f"El precio en dólares es: ${precio_dolares:,.2f}")
    return precio_dolares

print("Antes de la función")
resultado = precio_a_dolares(100, 18)
x = float(input("Indica el precio en pesos: "))
y = float(input("Indica el tipo de cambio: "))
resultado = precio_a_dolares(x, y)
print("Después de la función")