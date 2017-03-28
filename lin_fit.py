import numpy as np
import matplotlib.pyplot as plt


datos=np.loadtxt('fake_regression.txt')


x_train=datos[:75,0]
y_train=datos[:75,1]

x_test=datos[75:,0]
y_test=datos[75:,1]

ECP_train=np.zeros(20)
ECP_test=np.zeros(20)

def ECP(x,y,coeffs):
	y_g=0	
	for i in range(len(coeffs)):
		y_g=np.poly1d(coeffs)(x)
	sum=0
	for j in range(len(x)):
		sum=sum+(y[i]-y_g[i])**2
	return sum/len(y)

for i in range(20):
	coeffs=np.polyfit(x_train,y_train,i)
	ECP_train[i]=ECP(x_train,y_train,coeffs)
	ECP_test[i]=ECP(x_test,y_test,coeffs)

n=np.linspace(1,20,20)

plt.plot(n,ECP_train)
plt.plot(n,ECP_test)
plt.show()
	

