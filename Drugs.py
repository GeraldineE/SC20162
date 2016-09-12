import numpy as np 
import matplotlib.pyplot as plt

t=120
Q=np.zeros((t,1))
k=0.2
Q[0]=200
deltat=0.1

times=np.zeros((t,1))
times[0]=0.0

for i in range(1,t):	

	Q[i]=Q[i-1]-(deltat*k*Q[i-1])
	times[i]=times[i-1]+0.1
	
	

print Q

plt.plot(times,Q)
plt.show()



