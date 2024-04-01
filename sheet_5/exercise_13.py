import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from langevin_equation import langevin_equation, dS, maxwell_boltzmann
#continuum extrapolation method at langevin

#subpoint 1

def second_moment(x):
    x_sq = [xi**2 for xi in x]
    return np.mean(x_sq)

delta_taus = [0.1,0.05,0.01, 0.001, 0.0001, 0.00001]

def continuum_extrapolation():
    xs = [langevin_equation(delta_tau) for delta_tau in delta_taus]
    xs_sm = [second_moment(x) for x in xs]
    print(xs_sm)
    return xs_sm

def cont_ext_plot():
    xs_sm = continuum_extrapolation()
    plt.scatter(delta_taus, xs_sm)
    plt.show()

#cont_ext_plot()

#subpoint 2

def langevin_equation_v2(delta_tau : float):
    tau_max = 10
    N = int(tau_max/delta_tau)

    x = np.zeros(N)
    x[0] = 2
    
    for i in range(1,N):
        eta = np.random.normal(0,1)
        x_prime = x[i-1] - dS(x[i-1]) * delta_tau + eta * np.sqrt(2*delta_tau)
        x_next = x[i-1] - 0.5 * ( dS(x[i-1]) + dS(x_prime) ) * delta_tau + eta * np.sqrt(2*delta_tau)
        x[i] = x_next
    return x

def lang_equ_v2_plot():
    samples = langevin_equation_v2(0.001)
    x = np.linspace(0,10,1000)
    y = maxwell_boltzmann(x)
    plt.hist(samples,1000, density = True)
    plt.plot(x,y)
    plt.show()

#subpoint 2.1

def continuum_extrapolation_v2():
    xs = [langevin_equation_v2(delta_tau) for delta_tau in delta_taus]
    xs_sm = [second_moment(xs_i) for xs_i in xs]
    print(xs_sm)
    return xs_sm
def cont_ext_v2_plot():
    xs_sm = continuum_extrapolation_v2()
    plt.scatter(delta_taus, xs_sm)
    plt.show()

cont_ext_v2_plot()

#d =  xs_sm at delta_tau = 0 from linear regression

def calc_n(index, d, c):
    i = index
    delta_tau = delta_taus[i]
    return np.log( (xs_sm[i] - d) * 1/c) * 1/np.log(delta_tau)


