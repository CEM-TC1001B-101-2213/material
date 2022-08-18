# Grado escolar
edad = int(input("Indica tu edad: "))

if edad >= 3 and edad <= 5:
    print("Kinder")
else:
    if edad >= 6 and edad <= 11:
        print("Primaria")
    else:
        if edad >= 12 and edad <= 14:
            print("Secundaria")
        else:
            if edad >= 15 and edad <= 17:
                print("Preparatoria")
            else:
                if edad >= 18:
                    print("Profesional")
                    
if edad >= 3 and edad <= 5:
    print("Kinder")
elif edad >= 6 and edad <= 11:
    print("Primaria")
elif edad >= 12 and edad <= 14:
    print("Secundaria")
elif edad >= 15 and edad <= 17:
    print("Preparatoria")
elif edad >= 18:
    print("Profesional")
else: # Caso por default
    print("?")