import math as m
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import random
"""
Independence Metropolis Hasting sampler with non-symmetric proposal-distribution
"""
#Ref.: https://github.com/abdulfatir/sampling-methods-numpy/blob/master/Metropolis-Hastings.ipynb
#https://www.statlect.com/fundamentals-of-statistics/Metropolis-Hastings-algorithm#:~:text=The%20Metropolis%2DHastings%20algorithm%20is,to%20a%20given%20target%20distribution.

@np.vectorize
def maxwell_boltzmann(x):
    a = 1
    if x < 0:
        return 0
    else:
        pdf = (2/np.pi)**(1/2) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3 
        return pdf
    
def gaussian(x, x_0):
    a = 1
    return np.exp(- (x - x_0)**2 / (2*a**2)) / np.sqrt(2*np.pi)

#########################################

def sampler(N, sigma):

    x = np.zeros(N)
    x_rejected = []

    x[0] = 10

    for i in range(1,N):
        x_i = x[i-1]
        x_prop = np.random.normal(0,sigma,1)
        print(x_prop)
        A = min(1, ((maxwell_boltzmann(x_prop) * gaussian(x_i, x_prop)) / (maxwell_boltzmann(x_i) * gaussian(x_prop, x_i))))
        if A > random.random():
            x[i] = x_prop
        else:
            x[i] = x_i
            x_rejected.append(0)
    print("Acceptance rate -", (len(x)-len(x_rejected)) / N)
    return x


samples = sampler(N = 10000, sigma = 5)

x = np.linspace(0,10,1000)
y = maxwell_boltzmann(x)

plt.plot(x, y)
plt.hist(samples, 100, density = True, histtype ='bar')
plt.show()