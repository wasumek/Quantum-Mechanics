# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:02:17 2015

@author: Wasu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as sp
#from scipy.optimize import brenth, fsolve

plt.figure()

hbar  = 6.582119514e-16     # h/2pi in eV*s
me    = sp.m_e    # electron mass in kg


#const=hbar**2/(2*me)/(1e-10**2*e) # print(const) --> 3.81012337097
n=1    # ground-state        
#k1=pi/L
#E1=const*(n*k1**2)         # ground-state energy --> 3.760441e-01 eV

v0 =4
E= np.linspace(-v0,0,2000)

const=np.sqrt(2*me*(E+v0))/hbar
const2=np.sqrt(-2*me*E)/hbar


#def y1(E):
#    return const*np.sin(0.25*const*L/2)-const2*np.cos(0.25*const*L/2)
#def y2(E):
#    return const*np.cos(0.25*const*L/2)+const2*np.sin(0.25*const*L/2)


def y1(E):
    return (np.sqrt(2*me*(E+v0))/hbar)*np.sin(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)-(np.sqrt(-2*me*E)/hbar)*np.cos(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)
def y2(E):
    return (np.sqrt(2*me*(E+v0))/hbar)*np.cos(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)+(np.sqrt(-2*me*E)/hbar)*np.sin(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)


L = 5       #A˚  
plt.subplot(211)
plt.axhline(0, color='black')
plt.plot(E,y1(E),'r')
plt.plot(E,y2(E),'g')



'''x1= fsolve(y1,-4,args=E)
print x1'''

L = 20       #A˚  
plt.subplot(212)
plt.axhline(0, color='black')
plt.plot(E,y1(E),'r')
plt.plot(E,y2(E),'g')
 
# Solve of the root in range a to b
'''x = np.array([])
for a in range(-4,0):
    x = np.append(x,brenth(y2,a,0))   
    print x'''

plt.show()

# For an infinite potential well
'''for L in range(-4,0):
    Ener = (hbar**2)*10/(2*me*(L**2))
    print Ener

Ener = (hbar**2)*10/(2*me*(L**2))
print Ener'''