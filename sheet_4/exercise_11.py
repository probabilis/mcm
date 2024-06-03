import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from statsmodels.graphics.tsaplots import plot_acf
from tqdm import tqdm

#################################################################
#https://www.wikiwand.com/en/Autocorrelation

with open("datafile.txt") as f:
    data = [line.strip() for line in f.readlines()]

data = [float(i) for i in data[:-1]]

def acf():
    """
    module function for reference
    """
    plot_acf(pd.DataFrame(data))
    plt.show()

#################################################################

def blocking(data, numbers, Nb):
    """
    blocking function from Prof. Sexty
    """
    out = [np.mean(data[i*Nb : (i+1) * Nb]) for i in range( int(len(numbers) / Nb ))]
    return out


Nb_samples = np.arange(0,100000,100)

variances = np.zeros(len(data))

for n in tqdm(range(1, len(data))):
    if n in Nb_samples:
        blocked_data = blocking(data, data, Nb = n)
        var = np.var(blocked_data)
        variances[n] = var

x = np.linspace(10,100000,1000)
f = lambda x: 1/x

plt.title("autocorrelations of given dataset")
plt.plot(np.arange(len(data)),variances, label = "variances of blocked samples")
plt.ylabel("var($x$) of blocked samples")
plt.xlabel("$N_b$ sample size")
plt.plot(x, f(x), label = "$1/x$ function")
plt.ylim(0,np.max(variances))
plt.legend()
plt.tight_layout()
plt.show()