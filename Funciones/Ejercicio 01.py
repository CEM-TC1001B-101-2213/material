
def kilometros(millas):
    km = millas * 1.609
    return km

millas = float(input("Dame las millas que recorriste: "))
resultado = kilometros(millas)
print(f"{millas:,.2f} millas son {resultado:,.2f} kilómetros")