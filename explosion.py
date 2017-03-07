import numpy as np
import matplotlib.pyplot as plt

L=250
dx=2
T_f=0.1
P_atm=1.01325E5
rho_atm=1
e=1E13
gamma=1.4

def e_0(x,y,z):
	if x==L/(2*dx) and y==L/(2*dx) and z==L/(2*dx):
		return e
	else
		return P_atm/(rho*(gamma-1))

def dt
