import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
import scipy.optimize as so
from scipy.special import factorial
from sympy import *

fig=plt.figure()
ax = fig.add_subplot(111)


H = [1]
H.append( np.poly1d([ 2,0  ], variable = 'x'))
N = int(raw_input('Input n? :'))
print H[0], H[1]
for i in range(2,N+1):
    H.append( H[1]*H[i-1] - 2*(i-1)*H[i-2])
    print H[i]

x = np.arange(-3,3,0.01)
axes = plt.gca()
axes.set_xlim([-3,3])
axes.set_ylim([-50,50])
ax.plot(x,x/x,label='n=0',linewidth=2)

for i in range(1,len(H)):
    if i%2 == 0 :
        ax.plot(x,H[i](x),label='n=%s' % i,linewidth=2)
    else: ax.plot(x,H[i](x),label='n=%s' % i,linewidth=2.5, ls='-.')
ax.axvline(x=0.0,c="black",linewidth=0.5,zorder=0)
ax.axhline(y=0.0,c="black",linewidth=0.5,zorder=0)
plt.title('Hermite Polynomials')
plt.xlabel('$x$')
plt.ylabel('$H_n$($x$)')
ax.legend(loc = 4)

ax.grid(which='both')
ax.grid(b= True,which='minor',c = 'Black')
ax.grid(b= True,which='major',c ='Black') 

plt.savefig('Herbx0.pdf',bbox_inches=0)

plt.show()
