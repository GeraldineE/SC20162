import matplotlib.pyplot as plt 
import turtle
import random


#VERTICES

	
def Sierpinski(x1,y1,x2,y2,x3,y3,aleatorio):	
	
		#aleatorio=int(random.random()*3)
	if aleatorio==0:
		plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color = 'black') 
	elif aleatorio==1:	
		pmx1=(x1+x2)/2
		pmy1=(y1+y2)/2
	elif aleatorio==2:	
		pmx2=(x1+x3)/2
		pmy2=(y1+y3)/2
	elif aleatorio==3:	
		pmx3=(x2+x3)/2
		pmy3=(y2+y3)/2

		Sierpinski(x1, y1, pmx1, pmy1, pmx3, pmy3, aleatorio-1)       
        Sierpinski(x2, y2, pmx2, pmy2, pmx1, pmy1, aleatorio-1) 
        Sierpinski(x3, y3, pmx3, pmy3, pmx2, pmy2, aleatorio-1) 
    
	return


print 'Este programa dibuja el Triangulo de Sierpinski' 
print 'Debe introducir los siguientes parametos ' 
print ' (a) Introduzca 6 valores que seran las coordenadas del triangulo' 
print ' (b) Introduzca un valor de la etapa del nivel de recursion' 
print 
vx1 = float(raw_input('Escribir valor 1 ')) 
print 
vy2 = float(raw_input('Escribir valor 2 ')) 
print
vx2 = float(raw_input('Escribir valor 3 ')) 
print
vy2 = float(raw_input('Escribir valor 4 ')) 
print
vx3 = float(raw_input('Escribir valor 5 ')) 
print
vy3 = float(raw_input('Escribir valor 6 ')) 
print
n1 = abs(int(raw_input('Escriba la etapa del nivel que desea: '))) 
print 
print 
plt.figure('Sierpinski ')  
plt.suptitle('FRACTAL TRINGULO DE Sierpinski') 
Sierpinski(vx1,vy2,vx2,vy2,vx3,vy3,n1)  
plt.show() 