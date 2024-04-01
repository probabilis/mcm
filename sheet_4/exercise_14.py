import numpy as np
import matplotlib.pyplot as plt

a = 1

@np.vectorize
def maxwell_boltzmann(x):
    if x < 0:
        return 0
    else:
        pdf = (2/np.pi)**(1/2) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3 
        return pdf

@np.vectorize
def dS(x):

    return  x/(2*a**2) - 2/x + x

def langevin_equation(delta_tau : float):
    tau_max = 10
    N = int(tau_max / delta_tau)

    x = np.zeros(N)
    x[0] = 2
    
    for i in range(1,N):
        eta = np.random.normal(0,1,1)
        x_next = x[i-1] - delta_tau * dS(x[i-1]) + eta * np.sqrt(2 * delta_tau)
        x[i] = x_next
    print(x)
    return x


samples = langevin_equation(0.0001)

x = np.linspace(0,10,1000)
y = maxwell_boltzmann(x)

plt.plot(x, y)
plt.hist(samples, 100, density = True, histtype ='bar')
plt.show()
