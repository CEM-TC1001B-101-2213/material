def vocales(texto):
    contador = 0
    texto = texto.lower()
    for i in texto:
        if i in "aeiouáéíóú":
            contador = contador + 1
    return contador

def palabras(texto):
    # espacios = texto.count(" ") + 1
    espacios = len(texto.split())
    return espacios

texto = "Hola Aurora,   ¿cómo   te   ha ido en la escuela?"
total_vocales = vocales(texto)
print(f"El total de vocales es: {total_vocales}")
total_palabras = palabras(texto)
print(f"El total de palabras es: {total_palabras}")