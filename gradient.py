import numpy as np
import matplotlib.pyplot as plt


n=101
h=0.1
x=np.zeros(n)
y=np.zeros(n)
x[0]=0
y[0]=0

for i in range(n-1):	

	dx= 0.2*(x[i]-1)
	dy=y[i]+2


 	x[i+1]=x[i]-(h*dx)
 	y[i+1]=y[i]-(h*dy)

 	f=0.1*((x[i]-1)**2)+0.5*((y[i]+2)**2)

print x
print y
print f
