import turtle
#http://www.openbookproject.net/thinkcs/archive/python/thinkcspyesp3e_abandonado/cap03.html
# ATRIBUTOS DE LA VENTANA 
turtle.setup(800, 600)
wn = turtle.Screen()
#wn.bgcolor("lightgreen")
wn.title("TRIANGULO DE SIERPINSKI BY GERALDINE")

# instantiate (create) tess and set her attributes
lado = turtle.Turtle()
lado.color("hotpink")
lado.pensize(3)



# draw an equilateral triangle with lado
lado.forward(320)
lado.left(120)
lado.forward(320)
lado.left(120)
lado.forward(320)
lado.left(120)

# turn lado around and move her away from the origin
lado.right(180)
lado.forward(320)

# instantiate triangle
triangle = turtle.Turtle()
# make triangle draw a square
triangle.forward(200)
triangle.left(90)
triangle.forward(200)
triangle.left(90)
triangle.forward(200)
triangle.left(90)
triangle.forward(200)