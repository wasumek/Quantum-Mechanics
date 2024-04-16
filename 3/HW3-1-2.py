# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:38:49 2015

@author: Wasu
"""

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


v0 =4
L= np.arange(1e-10,5,0.1)


# For an infinite potential well
def Ener(n): 
    return (n**2)*(hbar**2)*(np.pi**2)/(2*me*(L**2))
#(4.276e-30/(2*me*(L**2))
#1.710e-29(2*me*(L**2)
# Even    
#y1(E)
#(np.sqrt(2*me*(E+v0))/hbar)*np.sin(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)-(np.sqrt(-2*me*E)/hbar)*np.cos(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)

# Odd
def y2(E):
    return (np.sqrt(2*me*(E+v0))/hbar)*np.cos(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)+(np.sqrt(-2*me*E)/hbar)*np.sin(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)

L=1
y1=(np.sqrt(2*me*((4.276e-30/(2*me*(L**2))+v0))/hbar)*\
np.sin(0.25*(np.sqrt(2*me*((4.276e-30/(2*me*(L**2))+v0))/hbar)*L/2)\
-(np.sqrt(-2*me*(4.276e-30/(2*me*(L**2)))/hbar)*np.cos(0.25*\
(np.sqrt(2*me*((4.276e-30/(2*me*(L**2))+v0))/hbar)*L/2)

print y1

plt.plot(L,y1,'r')

#y2=(np.sqrt(2*me*(E+v0))/hbar)*np.cos(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)+(np.sqrt(-2*me*E)/hbar)*np.sin(0.25*(np.sqrt(2*me*(E+v0))/hbar)*L/2)
#plt.plot(L,y2(L),'g')

plt.axhline(0, color='black')
plt.show()

