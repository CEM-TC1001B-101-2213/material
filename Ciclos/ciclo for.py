#import turtle as t

# range(número) -> Genera una secuencia numérica que inicia desde
# 0 y termina uno antes de número
for i in range(5):
    #t.forward(100)
    #t.left(360/5)
    print(f"El valor de i es: {i}")
#t.mainloop()
    
print("-------------------")

# range(inicio, final) -> Genera una secuencia numérica que inicia
# en inicio y termina uno antes de final
for i in range(3,8):
    print(f"El valor de i es: {i}")
    
print("-------------------")

# range(inicio, final, paso) -> Genera una secuencia numérica que inicia
# en inicio, termina uno antes de final y avanza de paso en paso
for i in range(3,8,2):
    print(f"El valor de i es: {i}")

print("-------------------")

for i in range(5,1,-1):
    print(f"El valor de i es: {i}")
    
print("-------------------")

texto = "Hola, ¿cómo estás?"
for i in texto:
    print(f"El valor de i es: {i}")
    
print("-------------------")

lista = [1, 2, "Hola", [7, 8], True]
for i in lista:
    print(f"El valor de i es: {i}")