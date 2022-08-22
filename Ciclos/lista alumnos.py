
alumnos = ["Juan", "María", "Jaime", "Pablo", "Carlos"]

nombre = input("Indica el nombre del alumno que deseas buscar: ")

encontrado = False
for i in alumnos:
    if nombre == i:
        encontrado = True
    
if encontrado == True:
    print("Se encontró al alumno.")
else:
    print("No se encontró al alumno.")
    
# Otra forma:
for i in alumnos:
    if nombre == i:
        print("Se encontró al alumno.")
        break # Rompe el ciclo
else: # Si no se rompió el ciclo:
    print("No se encontró al alumno.")