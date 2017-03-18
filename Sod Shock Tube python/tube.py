import numpy as np
import matplotlib.pyplot as plt
#===============================================================================
# Funciones
#===============================================================================
def u_0(): 
        return 0

def rho_0(x):
    if x<=0.5:
        return 1
    else:
        return 0.125

def P_0(x):
        if x<=0.5:
            return 1
        else:
            return 0.1
def e_0(x):
    return P_0(x)/0.4+0.5*rho_0(x)*u_0()**2    

def Mac_Cormack(Xmax, tmax, dx, dt):
    I=int(Xmax/dx)
    N=int(tmax/dt)
    
    U1=np.zeros([N,I])
    U2=np.zeros([N,I])
    U3=np.zeros([N,I])
    
    F1=np.zeros([N,I])
    F2=np.zeros([N,I])
    F3=np.zeros([N,I])
    
    #Condiciones iniciales
    for i in range(I):
        U1[0][i]=rho_0(i*dx)
        U2[0][i]=rho_0(i*dx)*u_0()
        U3[0][i]=e_0(i*dx)
        F1[0][i]=u_0()*rho_0(i*dx)
        F2[0][i]=e_0(i*dx)*u_0()**2+P_0(i*dx)
        F3[0][i]=u_0()*(e_0(i*dx)+P_0(i*dx))
        
    #Condiciones de frontera
    for n in range(N):
        U1[n][0]=rho_0(0)
        U2[n][0]=rho_0(0)*u_0()
        U3[n][0]=e_0(0)
        F1[n][0]=u_0()*rho_0(0)
        F2[n][0]=e_0(0)*u_0()**2+P_0(0)
        F3[n][0]=u_0()*(e_0(0)+P_0(0))
        U1[n][I-1]=rho_0(I-1)
        U2[n][I-1]=rho_0(I-1)*u_0()
        U3[n][I-1]=e_0(I-1)
        F1[n][I-1]=u_0()*rho_0(I-1)
        F2[n][I-1]=e_0(I-1)*u_0()**2+P_0(I-1)
        F3[n][I-1]=u_0()*(e_0(I-1)+P_0(I-1))
    
    #recorrido en el tiempo
    for n in range(N-1):
        U1m=np.zeros(I)
        U2m=np.zeros(I)
        U3m=np.zeros(I)
        F1m=np.zeros(I)
        F2m=np.zeros(I)
        F3m=np.zeros(I)
        #Calcula valores en tiempo intermedio (*)
        for i in range(I-1):
            if i!=0:
                U1m[i]=U1[n][i]-dt/dx*(F1[n][i+1]-F1[n][i])
                U2m[i]=U2[n][i]-dt/dx*(F2[n][i+1]-F2[n][i])
                U3m[i]=U3[n][i]-dt/dx*(F3[n][i+1]-F3[n][i])
            
                F1m[i]=U2m[i]
                F2m[i]=(U2m[i]**2)/U1m[i]+0.4*(U3m[i]-U2m[i]**2/U1m[i]*0.5)
                F3m[i]=U2m[i]/U1m[i]*(U3m[i]-0.4*(U3m[i]-U2m[i]**2/U1m[i]*0.5))
        #Calcula valores en tiempo n+1      
        for i in range(I-1):
            if i!=0:
                U1[n+1][i]=0.5*(U1[n][i]+U1m[i]-dt/dx*(F1m[i]-F1m[i-1]))
                U2[n+1][i]=0.5*(U2[n][i]+U2m[i]-dt/dx*(F2m[i]-F2m[i-1]))
                U3[n+1][i]=0.5*(U3[n][i]+U3m[i]-dt/dx*(F3m[i]-F3m[i-1]))
            
                F1[n+1][i]=U2[n+1][i]
                F2[n+1][i]=U2[n+1][i]**2/U1[n+1][i]+0.4*(U3[n+1][i]-U2[n+1][i]**2/U1[n+1][i]*0.5)
                F3[n+1][i]=U2[n+1][i]/U1[n+1][i]*(U3[n+1][i]-0.4*(U3[n+1][i]-U2[n+1][i]**2/U1[n+1][i]*0.5))
    return [U1[N-1],U2[N-1],U3[N-1]]


#===============================================================================
# Ejecucion de Differencias finitas para sod shock tube
#===============================================================================
tmax = [0.01,0.05,0.07,0.2, 0.4]
Xmax = 1
dx = 0.1
dt = 0.01


for t in tmax:

        I=int(Xmax/dx)
        N=int(t/dt)
    
        U1=np.zeros([N,I])
        U2=np.zeros([N,I])
        U3=np.zeros([N,I])

        u=np.zeros([N,I])
        rho=np.zeros([N,I])
        P=np.zeros([N,I])

        x=np.linspace(0,1,I)

        U=Mac_Cormack(Xmax, t, dx, dt)
        U1=U[0]
        U2=U[1]
        U3=U[2]
        u=U2/U1
        rho=U1
        P=0.4*(U3-0.5*rho*u**2)
        #print("plotting for ")
        #print(t)
        #print(U1)
        plt.plot(x,u)

plt.show()