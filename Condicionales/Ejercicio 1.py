
print("Para las siguientes preguntas, responde 1 para sí y 2 para no")
respuestas_sí = 0

pregunta = int(input("¿Actúas ética e irreprochablemente en tu trabajo?: "))
if pregunta == 1:
    respuestas_sí = respuestas_sí + 1
    
pregunta = int(input("¿Tu honradez y sinceridad proporcionan confianza a las demás personas de tu entorno laboral? :"))
if pregunta == 1:
    respuestas_sí = respuestas_sí + 1
    
pregunta = int(input("¿Eres capaz de admitir tus propios errores?: "))
if pregunta == 1:
    respuestas_sí = respuestas_sí + 1
    
pregunta = int(input("¿Señalas las acciones poco éticas de los demás sin miedo a enfrentarte a las injusticias?: "))
if pregunta == 1:
    respuestas_sí = respuestas_sí + 1
    
pregunta = int(input("¿Adoptas posturas firmes y fundamentadas en tus principios, aunque resulten impopulares? : "))
if pregunta == 1:
    respuestas_sí = respuestas_sí + 1
    
if respuestas_sí < 4:
    print("Hay algunos puntos a mejorar en tu actuar.")
else:
    print("Eres una persona laboralmente confiable.")