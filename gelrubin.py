import numpy as np
import matplotlib.pyplot as plt


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

def PLX(l):
	i=int((l-lambda_min)/(lambda_max-lambda_min)*N)
	if i<0 or i>=N:
		return 0
	else:
		return Plx[i]

def MetHas(sigma):
	nl=[np.random.random()*10.0]
	Nl=100000
	for i in range(1,Nl):
		l_new=np.random.normal(nl[i-1],sigma)
		alpha=min(1,PLX(l_new)/PLX(nl[i-1]))
	
		u=np.random.random()
		if alpha>u:
			nl.append(l_new)
		else:
			nl.append(nl[i-1])
	return nl


def norm(P):
	c=0
	for i in range(len(P)):
		c=c+P[i]*(lambda_max-lambda_min)/N
	return c

lambda_min=0.1
lambda_max=10
l=np.linspace(lambda_min,lambda_max,N)

X=np.array([1.5,1.7,2.0])
Plx=np.zeros(len(l))
for i in range(len(l)):
	Plx[i]=vero(X,l[i])*probL(l[i],lambda_min,lambda_max)


def prom(a):
	return float(sum(a))/len(a)
def var(a):
	prom=prom(a)
	c=0
	for i in a:
		c=c+pow(i-prom,2)
	return c/(len(a)-1)
	

plt.hist(MetHas(1), bins=50, normed=True)
plt.plot(l,Plx/norm(Plx))
plt.show()
		

