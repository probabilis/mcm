import math as m
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt

#########################################
#Ref.: https://towardsdatascience.com/what-is-rejection-sampling-1f6aff92330d

def maxwell_boltzmann(x):
    a = 1
    pdf = (2/np.pi)**(1/2) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3 
    return pdf


def sampler(use_gauss_proposal, f, a, b,f_max, N = 1_000_000):
    prop_norm = scipy.stats.norm(loc = 2, scale = 1)
    prop_uni = scipy.stats.uniform(-a, a + b)
    
    if use_gauss_proposal:
        C = 2.1
        X = np.random.randn(N)
        u = np.random.uniform(0, C * prop_norm.pdf(X))

    else:
        C = f_max /(1/(b-a)) 
        X = np.random.uniform(a, b, size = N)
        u = np.random.uniform(0, C * prop_uni.pdf(X))

    samples = X[u <= f(X)]
    samples = [x for x in samples if x >= 0]

    print("Acceptance rate -", len(samples) / N)
    return samples

a = 0 ; b = 10

x = np.linspace(a,b,1000)

def plot_uniform_vs_normal():
    #norm = scipy.stats.norm(loc = 0, scale = 1)
    #plt.plot(x, norm.pdf(x) * (2*np.pi)**(1/2) * f_max, color = "k")

    samples_normal = sampler(True, maxwell_boltzmann, a, b, np.max(maxwell_boltzmann(x)))
    samples_uniform = sampler(False, maxwell_boltzmann, a, b, np.max(maxwell_boltzmann(x)))

    fig, axs = plt.subplots(1,2)

    axs[0].plot(x,maxwell_boltzmann(x))
    axs[1].plot(x,maxwell_boltzmann(x))

    axs[0].hist(samples_normal, 1000, density = True, histtype ='bar')
    axs[1].hist(samples_uniform, 1000, density = True, histtype ='bar')

    plt.show()

def multiple_samples(sample_size):

    df = pd.DataFrame(columns = ["mean", "variance","skewness", "true_mean", "true_variance","true_skewness"])
    
    a = 1

    mean = 2 * a * np.sqrt(2/np.pi)
    variance = a**2 * (3*np.pi - 8)/np.pi
    skewness = 2 * np.sqrt(2) * (16 - 5 * np.pi)/(3*np.pi - 8)**(3/2)
    
    for i in range(sample_size):
        samples = sampler(False, maxwell_boltzmann, a, b, np.max(maxwell_boltzmann(x)))

        df.loc[i] = [np.mean(samples), np.var(samples), scipy.stats.skew(samples),mean, variance, skewness ]
    return df


if __name__ == "__main__":

    plot_uniform_vs_normal()

    sample_size = 50
    df = multiple_samples(sample_size)
    print(df)
    variances = np.var(df["mean"])
    print(f"The variance of {sample_size} samples is :", variances)
