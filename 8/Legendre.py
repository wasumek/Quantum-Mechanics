import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(111)
L = [1]
L.append( np.poly1d([1,0], variable = 'x'))
N = int(raw_input('n = '))
print L[0], L[1]
for i in range(2,N+1):
    L.append(( (2*i-1) *L[1] *L[i-1] - (i-1) *L[i-2] )/i)
    print L[i]

x = np.arange(-1,1,0.01)
axes = plt.gca()
axes.set_xlim([-1,1])
axes.set_ylim([-1.2,1.2])
ax.plot(x,x/x,label='n=0',linewidth=2)

for i in range(1,len(L)):
    if i%2 == 0 :
        ax.plot(x,L[i](x),label='n=%s' % i,linewidth=2)
    else: ax.plot(x,L[i](x),label='n=%s' % i,linewidth=2.5, ls='-.')
ax.axvline(x=0.0,c="black",linewidth=0.5,zorder=0)
ax.axhline(y=0.0,c="black",linewidth=0.5,zorder=0)
plt.title('Legendre Polynomials')
plt.xlabel('$x$')
plt.ylabel('$L_n$($x$)')
ax.legend(loc = 4)

ax.grid(which='both')
ax.grid(b= True,which='minor',c = 'Black')
ax.grid(b= True,which='major',c ='Black') 

plt.savefig('LegenP.pdf',bbox_inches=0)

plt.show()
