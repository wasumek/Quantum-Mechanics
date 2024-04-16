# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:41:19 2015

@author: Wasu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as sp

plt.figure()

hbar  = 6.582119514e-16     # h/2pi in eV*s
me    = sp.m_e    # electron mass in kg
v0 = 2  # in eV
a = 5 # Angstroms
E = np.linspace(0,6,2000)

#k1 = (np.sqrt(2*me*E)/hbar) 
#k2 = (np.sqrt(2*me*(v0-E))/hbar)

#k1 = (sqrt(2*9.10938291e-31*E)/6.582119514e-16) 
#k2 = (sqrt(2*9.10938291e-31*(6-E))/6.582119514e-16)


def T(E):
    return (4*((np.sqrt(2*me*E)/hbar)**2)*((np.sqrt(2*me*(v0-E))/hbar)**2))/(4*((np.sqrt(2*me*E)/hbar)**2)*((np.sqrt(2*me*(v0-E))/hbar)**2)*((np.cos((np.sqrt(2*me*(v0-E))/hbar)*a))**2)+((((np.sqrt(2*me*E)/hbar)**2)+((np.sqrt(2*me*(v0-E))/hbar)**2))**2)*((np.sin((np.sqrt(2*me*(v0-E))/hbar)*a))**2))

def T2(E):
    return (4*((np.sqrt(2*me*E)/hbar)**2)*((np.sqrt(2*me*(E-v0))/hbar)**2))/(4*((np.sqrt(2*me*E)/hbar)**2)*((np.sqrt(2*me*(E-v0))/hbar)**2)*((np.cos((np.sqrt(2*me*(E-v0))/hbar)*a))**2)+((((np.sqrt(2*me*E)/hbar)**2)+((np.sqrt(2*me*(E-v0))/hbar)**2))**2)*((np.sin((np.sqrt(2*me*(E-v0))/hbar)*a))**2))


plt.plot(E,T(E),'r')
plt.plot(E,T2(E),'r')

plt.show()

