
total = 0
precio = 0
while precio >= 0:
    total = total + precio
    precio = float(input("Indica el precio de tu producto: "))
print(f"El total a pagar es: ${total:,.2f}")