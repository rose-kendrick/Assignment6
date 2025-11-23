import numpy as np
from matplotlib import pyplot as pp

def V(r1,r2):
    V = ((k*q1)/r1)-((k*q2)/r2)
    return V


epsilon_0 = 8.854e-12
k = 1/(4*np.pi*epsilon_0)
q1 = 1 #C
q1x = -0.05 #m
q1y = 0 #m 
q2 = -1 #C
q2x = 0.05 #m
q2y = 0 #m

x = np.arange(-0.1,0.101,0.001) 
y = np.arange(-0.1,0.101,0.001)
X,Y = np.meshgrid(x,y)

r1x = X-q1x
r1y = Y-q1y
r1 = np.sqrt((r1x)**2+(r1y)**2)

r2x = X-q2x
r2y = Y-q2y
r2 = np.sqrt((r2x)**2+(r2y)**2)

rmin = 0.001 #m
r1[r1 <= rmin] = rmin
r2[r2 <= rmin] = rmin

Vdist = V(r1,r2)

pp.figure()
potential = pp.contourf(X,Y,Vdist,levels=100,cmap='Blues_r')
pp.xlabel('x position (m)')
pp.ylabel('y position (m)')
colorbar = pp.colorbar(potential, label='Potential (V)')
#pp.show()
pp.savefig('potential.png')

