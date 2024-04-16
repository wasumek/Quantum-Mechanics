# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:54:29 2015

@author: Wasu
"""

import matplotlib.pyplot as plt
import numpy as np
import math as mt

L = 1
Z = np.linspace(0,1,num=100)
t = np.linspace(0,1,num=100)

#Expo = mt.exp(iwt)
W= []

for z in Z:
    F1 = 10*mt.sqrt(2/L)*mt.sin(mt.pi*z/L)
    F2 = -5*mt.sqrt(2/L)*mt.sin(3*mt.pi*z/L)
    F3 = mt.sqrt(2/L)*mt.sin(5*mt.pi*z/L)
    ans = ((1/mt.sqrt(126))*(F1+F2+F3))**2
    W.append(ans)
    
plt.plot(Z,W)




plt.show()
