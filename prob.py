import numpy as np
import matplotlib.pyplot as plt

lambda_min=0.1
lambda_max=10
a=1
b=20
N=1000.
def vero(X, lam):
	prob=1;
	for i in range(len(X)):
		prob=prob*np.exp(-X[i]/lam)/(-lam*(np.exp(-b/lam)-np.exp(-a/lam)))
	return prob

def probL(l,lmin, lmax):
	return 1./(lmax-lmin)

l=np.linspace(lambda_min,lambda_max,N)

X=np.array([1.5,1.7,2.0])
Plx=np.zeros(len(l))
for i in range(len(l)):
	Plx[i]=vero(X,l[i])*probL(l[i],lambda_min,lambda_max)

elmax=0
pmax=0
for i in range(len(l)):
	if(Plx[i]>elmax):
		elmax=Plx[i]
		pmax=i*(lambda_max-lambda_min)/N

c=0
for i in range(len(Plx)):
	c=c+Plx[i]*(lambda_max-lambda_min)/N
print c

def PLX(l):
	i=int((l-lambda_min)/(lambda_max-lambda_min)*N)
	if i<0 or i>=N:
		return 0
	else:
		return Plx[i]

nl=[0.1]
delta=0.1
Nl=20000
for i in range(1,Nl):
	U=np.random.random()*2*delta-delta
	l_new=nl[i-1]+U
	alpha=min(1,PLX(l_new)/PLX(nl[i-1]))
	
	u=np.random.random()
	if alpha>u:
		nl.append(l_new)
	else:
		nl.append(nl[i-1])

plt.hist(nl, bins=50, normed=True)
plt.plot(l,Plx/c)
plt.show()
		

