import numpy as np
import matplotlib.pyplot as plt

def likelihood(q):
	return np.exp(-q*q)

def loglike(q):
	return -q*q

def der_loglike(q):
	return -2*q

def leapfrog(q,p, delta_t=1E-3,n=5):
	q_new=q
	p_new=p	
	for i in range(n):
		p_new= p_new +0.5*delta_t*der_loglike(q_new)
		q_new=q_new+delta_t*p_new
		p_new=p_new+0.5*delta_t*der_loglike(q_new)
	return q_new, -p_new

def H(q,p):
	K= 0.5*p*p
	U=-loglike(q)
	return K+U

def MCMC(nsteps):
	q=np.zeros(nsteps)
	p=np.zeros(nsteps)
	p[0]= np.random.normal(0,1)
	q[0]=np.random.normal(0,1)
	E=H(q[0],p)
	for i in range(1,nsteps):
		p[i]=np.random.normal(0,1)
		q_new, p_new=leapfrog(q[i-1],p[i-1])
		E_new=H(q_new,p_new)
		E_old=H(q[i-1],p[i-1])
		alpha=min(1,np.exp(-E_new+E_old))
		beta=np.random.random()
		if(beta<alpha):
			q[i]=q_new
		else:
			q[i]=q[i-1]
	return q
		
q_chain=MCMC(10000)
plt.hist(q_chain[500:],bins=20)
plt.show()
	
