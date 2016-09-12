#Este codigo fue sacado de la pagina de internet:
#http://www.investigacionyciencia.es/blogs/matematicas/33/posts/bifurcaciones-12410
#Consiste en la ecuacion de Bifurcacion del mapa logistico

import numpy as np
import matplotlib.pyplot as plt

def mapa(r,x):

    der = r*(1.-2.*x)
    return r*x*(1.-x), der

def lyap(r, x):

    xcp = x
    acum = 0.
    der  = 0.
    (xcp,der)  = mapa(r,xcp)
    for i in range(100):
        if (der != 0.):
            acum = acum + np.log(np.abs(der))
        (xcp,der)  = mapa(r,xcp)

    return acum/100.


x      = input("Entra el valor de la poblacion inicial:     ")
r      = input("Entra el valor del parametro r:             ")
npasos = input("Entra el numero de generaciones a calcular: ")


xa=np.zeros(npasos)
xa[0]=x

for i in range(0,npasos-1):
    (xa[i+1],foo) = mapa(r,xa[i])
    print xa[i]

plt.xlabel("pasos")
plt.ylabel("Poblacion")
plt.title("Parametro r=" + str(r))
plt.plot(xa, 'ro-')
plt.grid(True)
plt.show()
