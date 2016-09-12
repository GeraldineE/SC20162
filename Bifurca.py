import numpy as np
import matplotlib.pyplot as plt

n=500
r=3.8
x=np.zeros((n,1))
x[0]=0.4

for i in range(1,n):
	x[i]=r*x[i-1]*(1-x[i-1])

print x
plt.plot(x)
plt.show()




