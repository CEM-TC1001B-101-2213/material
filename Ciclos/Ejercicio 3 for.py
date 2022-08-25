
numero_ingresos = int(input("Indica la cantidad de ingresos de la empresa: "))

total_ingresos = 0

for i in range(1, numero_ingresos+1):
    monto = float(input(f"Indica el monto del ingreso {i}: "))
    total_ingresos = total_ingresos + monto

numero_gastos = int(input("Indica la cantdad de gastos de la empresa: "))

total_gastos = 0

for i in range(1, numero_gastos+1):
    monto = float(input(f"Indica el monto del gasto {i}: "))
    total_gastos = total_gastos + monto
    
balance = total_ingresos - total_gastos

print(f"El total de ingresos fue de: ${total_ingresos:,.2f}")
print(f"El total de gastos fue de: ${total_gastos:,.2f}")
print(f"El balance de la empresa es de: ${balance:,.2f}")

if total_gastos > total_ingresos:
    print("La empresa está en números rojos.")
elif total_gastos == total_ingresos:
    print("La empresa está en números negros.")
else:
    print("La empresa está en números azules.")