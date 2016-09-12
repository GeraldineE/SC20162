#Grafica del triangulo de Sierpinski

import matplotlib.pyplot as plt 
import turtle
import random as ran




#FUNCION RECURSIVA 
def Triangulo(x1,y1,x2,y2,x3,y3,n):
    
    if n==0:    
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color = 'black')#Grafica el triangulo base
    elif n==1:   
        pmx1=(x1+x2)/2
        pmy1=(y1+y2)/2
    elif n==2:  
        pmx2=(x1+x3)/2
        pmy2=(y1+y3)/2
    elif n==3:  
        pmx3=(x2+x3)/2
        pmy3=(y2+y3)/2  

        Triangulo(x1, y1, pmx1, pmy1, pmx3, pmy3, n-1)       
        Triangulo(x2, y2, pmx2, pmy2, pmx1, pmy1, n-1) 
        Triangulo(x3, y3, pmx3, pmy3, pmx2, pmy2, n-1) 
    
    return 


# FUNCION PRINCIPAL
def main():
    plt.figure('Triangulo de Sierpinski') 
    plt.suptitle('By Geraldine Echavarria') # subtitulo 
    Triangulo(1,1,2,3,3,1,ran.randint(0,3)) #Le quemo por defecto los valores de las coordenadas de los puntos del triangulo base
    #ran.randint(0,3), Genera un aleatorio entre 0 y 3 
    plt.show()




# Inicia el programa
if __name__=='__main__':
    main()