import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#################################################
#defined functions

def compute_vol_ball(d, n):
    samples_df = pd.DataFrame(np.random.rand(n, d))
    norm_d = (samples_df**2).sum(axis=1)
    is_in_ball = norm_d < 1
    vol = 2**d * (is_in_ball.sum() / n)
    return vol

def pi_from_vol(n):
    r = 1
    V = compute_vol_ball(10, n)
    sampled_pi = (V * 120 / r**10)**(1/5)
    return sampled_pi

#################################################

def single_calculated_pi() -> None:
    n = 100
    result = pi_from_vol(n)
    print(np.pi)
    print("Pi through sampling : ", result)

single_calculated_pi()

def sampling_for_pi(N : int):
    pi_est = np.zeros(N)
    if type(N) == int:
        for k in range(1, N): 
            pi_est[k] = pi_from_vol(k)
        average = np.mean(pi_est)
        var = np.var(pi_est) 
    else:
        print("Calculating PI did not work.")
        
    print(f"The calculated value of pi is : {average} with a delta to the original value of: {abs(np.pi - average)}")
    return average, var

def multiple_samples(Ns):

    pi_array = np.zeros(len(Ns))
    var_array = np.zeros(len(Ns))

    for i, N in enumerate(Ns):
        try:
            pi_array[i], var_array[i] = sampling_for_pi(int(N))
        except TypeError:
            pi_array[i], var_array[i] = 0, 0
            print("Error")

    return pi_array, var_array

def multiple_samples_plot() -> None:

    Ns = np.arange(1000,10000, 1000)
    pis, vars_ = multiple_samples(Ns)
    
    
    print(vars_)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(Ns, pis)
    ax1.set_title("Pi mean values over different sample sizes $N_s$")
    ax1.set_xlabel("$N_s$")
    ax1.set_ylabel("<pi>")

    ax2.plot(Ns, np.sqrt(vars_))
    ax2.set_title("Variance of Pi values over different sample sizes $N_s$")
    ax2.set_xlabel("$N_s$")
    ax2.set_ylabel("$\sigma(pi)$ value")
    fig.tight_layout()
    plt.savefig("exercise_02_plot.png")
    plt.show()


multiple_samples_plot()