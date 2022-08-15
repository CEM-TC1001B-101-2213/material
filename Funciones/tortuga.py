import turtle as t

def cuadrado(tamaño):
    t.forward(tamaño)
    t.left(90)
    t.forward(tamaño)
    t.left(90)
    t.forward(tamaño)
    t.left(90)
    t.forward(tamaño)
    t.left(90)
    
cuadrado(100)
cuadrado(50)

t.mainloop()