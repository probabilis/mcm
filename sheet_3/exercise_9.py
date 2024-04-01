import math as m
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import random
"""
Metropolis sampler with symmetric proposal distribution
"""
#Ref.: https://stephens999.github.io/fiveMinuteStats/MH_intro.html

@np.vectorize
def maxwell_boltzmann(x):
    a = 1
    if x < 0:
        return 0
    else:
        pdf = (2/np.pi)**(1/2) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3 
        return pdf

#########################################

def sampler(N, sigma):

    x = np.zeros(N)
    x_rejected = []

    x[0] = 1

    for i in range(1,N):
        x_i = x[i-1]
        x_prop = x_i + np.random.normal(0,sigma,1)
        A = min(1, maxwell_boltzmann(x_prop) / maxwell_boltzmann(x_i))
        if random.random() < A:
            x[i] = x_prop
        else:
            x[i] = x_i
            x_rejected.append(0)
    print("Acceptance rate -", (len(x)-len(x_rejected)) / N)
    return x

samples = sampler(N = 10000, sigma = 1)

x = np.linspace(0,10,1000)
y = maxwell_boltzmann(x)

plt.plot(x, y)
plt.hist(samples, 100, density = True, histtype ='bar')
plt.show()

#########################################

def multiple_sigmas():

    a = 1
    N = 10000
    sigmas = [0.1, 0.5, 1, 2, 3]

    mean = 2 * a * np.sqrt(2/np.pi)
    variance = a**2 * (3*np.pi - 8)/np.pi
    skewness = 2 * np.sqrt(2) * (16 - 5 * np.pi)/(3*np.pi - 8)**(3/2)

    df = pd.DataFrame(columns = ["mean", "variance","skewness", "true_mean", "true_variance","true_skewness"], index = sigmas)

    for i in range(len(sigmas)):

        samples = sampler(N, sigmas[i])
        df.loc[i] = [np.mean(samples),np.var(samples),scipy.stats.skew(samples), mean, variance, skewness]

    return df

df = multiple_sigmas()
print(df)

