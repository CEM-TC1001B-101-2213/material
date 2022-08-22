
numero_articulos = int(input("¿Cuántos artículos distintos se ingresarán?: "))

if numero_articulos < 0:
    print("Debe ingresar una cantidad positiva de artículos.")
else:
    total = 0
    for i in range(1, numero_articulos+1):
        precio = float(input(f"Precio del artículo {i}: "))
        cantidad = float(input(f"Cantidad de artículos {i}: "))
        total = total + precio * cantidad
    print(f"El total a pagar es de ${total:,.2f} pesos.")