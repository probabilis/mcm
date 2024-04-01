import numpy as np
import matplotlib.pyplot as plt

#################################################
#defined functions

def sampling_for_pi(N : int):

    circles = 0 ; squares = 0
    xi = np.zeros(N)
    pi_est = np.zeros(N)

    if type(N) == int:
        for k in range(0, N): 
            x = np.random.uniform(0,1)
            y = np.random.uniform(0,1)   

            norm = np.sqrt(x**2 + y**2)
            xi[k] = norm
        
            if norm <= 1: circles += 1
            squares += 1
            pi_est[k] = 4 * circles/squares

        average = np.mean(pi_est)
        var = np.var(pi_est)#1 / (N - 1) * np.sum(xi - average) 
        pi = 4 * circles / squares
    else:
        print("Calculating PI did not work.")
        
    print(f"The calculated value of pi is : {pi} with a delta to the original value of: {abs(np.pi - pi)}")
    return pi, var

#################################################

Ns = np.arange(1000,10e4, 1000)

def multiple_samples(Ns):

    pi_array = np.zeros(len(Ns))
    var_array = np.zeros(len(Ns))

    for i, N in enumerate(Ns):
        pi_array[i], var_array[i] = sampling_for_pi(int(N))

    return pi_array, var_array

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
plt.savefig("exercise_01_plot.png")
plt.show()
