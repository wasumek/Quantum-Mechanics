"""
Created on Wed 20 Jan, 2016
@author: Wasu
"""
from numpy import linspace
import matplotlib.pyplot as plt
from sympy.physics.hydrogen import R_nl
from sympy.utilities.lambdify import lambdify
from sympy.abc import x
fn_10 = lambdify(x, R_nl(1,0,x,1), 'numpy')
fn_20 = lambdify(x, R_nl(2,0,x,1), 'numpy')
fn_30 = lambdify(x, R_nl(3,0,x,1), 'numpy')
fn_21 = lambdify(x, R_nl(2,1,x,1), 'numpy')
fn_31 = lambdify(x, R_nl(3,1,x,1), 'numpy')
fn_32 = lambdify(x, R_nl(3,2,x,1), 'numpy')
xx = linspace(0,30,num=1000)
plt.plot(xx, fn_10(xx)*xx, label='n=1,l=0')
plt.plot(xx, fn_20(xx)*xx, label='n=2,l=0')
plt.plot(xx, fn_30(xx)*xx, label='n=3,l=0')
plt.plot(xx, fn_21(xx)*xx, label='n=2,l=1')
plt.plot(xx, fn_31(xx)*xx, label='n=3,l=1')
plt.plot(xx, fn_32(xx)*xx, label='n=3,l=2')
plt.axis([0,30,-0.5,0.9])
plt.axhline(0, color='black')
plt.title('The Radial Wave Functions ($u_{n,l}$)')
plt.xlabel('Radial distance')
plt.ylabel('Wave function ($u_{n,l}$)')
plt.legend(loc=1)
plt.show()
