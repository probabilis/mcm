import math as m
import numpy as np
import matplotlib.pyplot as plt

def maxwell_boltzmann(x):
    a = 1
    pdf = (2/np.pi)**(1/2) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3 
    return pdf

def gaussian(x, mu, sigma):
    pdf = 1 / (sigma * (2*np.pi)**(1/2)) * np.exp( -0.5 * ((x - mu)/sigma)**2 )
    return pdf


def main(a,b, max_samples):

    samples = []

    while len(samples) < max_samples:

        rand_norm = np.random.normal(0,1,1)
        rand = np.random.uniform(a,b)

        if rand_norm * rand * gaussian(rand_norm,0,1) < maxwell_boltzmann(rand_norm):
            samples.append(rand_norm)

    return np.array(samples)

samples = main(0,10, 10000)
print(samples)

#x = np.linspace(-1,1,100)
#plt.plot(x, gaussian(x,0,1))
plt.hist(samples, 1000, density = True, histtype ='bar')
plt.show()