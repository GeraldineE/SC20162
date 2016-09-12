import turtle

# ATRIBUTOS DE LA VENTANA 
turtle.setup(800, 600)
ventana = turtle.Screen()
ventana.title("TRIANGULO DE SIERPINSKI BY GERALDINE")

#Objeto triangulo hace referencia a clase Turtle
triangulo = turtle.Turtle()

#Funcion recursiva
def sierpinski(n):  
    if n>1:
        for i in range(3):  
            sierpinski(.5*n)
            triangulo.forward(n)
            triangulo.left(120)
            triangulo.speed(50)
sierpinski(400)  

    
