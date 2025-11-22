import numpy as np
from matplotlib import pyplot as pp


def f(x):
    y = 2+0.75*np.tan(2*x)
    return y

def f_prime(x,dx):
    y = (f(x+dx)-f(x-dx))/(2*dx)
    return y

def realfPrime(x):
    y = 1.5/(np.cos(2*x))**2 
    return y

dx = [1,0.5,0.1]

for n in range(len(dx)):
    x = np.arange(-2,2+dx[n],dx[n])
    fPrime = []
    for i in range(len(x)):
        fP = f_prime(x[i],dx[n])
        fPrime.append(fP)

    pp.figure()
    pp.plot(x,f(x),color='blue')
    pp.plot(x,fPrime,color='orange')
    pp.plot(x,realfPrime(x),linestyle='dashed')
    pp.show()



