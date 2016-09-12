
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


xini = 0.45565665

npasos=1000
niter=100
xa=np.zeros((npasos*niter))
r=np.zeros((npasos*niter))

r1 = input("Entra el valor de r min:   ")
r2 = input("Entra el valor de r max:   ")


h=(r2-r1)/(npasos-1)
for i in range(0,npasos):
    r[niter*i] = r1+i*h 
    x=xini
    for j in range(0,10000):
        (x,foo) = mapa(r[i*niter],x)
    
    xa[niter*i]=x
    for j in range(0,niter-1):
        r[i*niter+j+1] = r1+i*h
        (xa[i*niter+j+1],foo) = mapa(r[i*niter],xa[i*niter+j])

           
plt.xlabel("pasos")
plt.ylabel("Poblacion")
plt.title("Parametro r=" + str(r[0]) + '-' + str(r[niter*npasos-1]))
#for i in range(0,npasos):
plt.plot(r,xa, 'r.',markersize=0.5)
plt.grid(True)
plt.show()