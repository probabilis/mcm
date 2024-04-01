import numpy as np
import matplotlib.pyplot as plt
from main import city_map, metropolis

#calculate mean and variance for same M and Ns for different cities
def main_fixed_config(iterations, num_cities):

    N_s = 1000
    M = 1000
    
    cities = city_map(num_cities)

    best_energies = []

    for _ in range(iterations):
        best_tour, best_energy = metropolis(cities, M, N_s)
        best_energies.append(best_energy)
    
    iter_ls = [str(i+1) for i in range(iterations)]
    
    energy_mean = np.mean(best_energies)
    energy_var = np.var(best_energies)
    print(f"The best energy average is: {energy_mean} and variance is: {energy_var}")

    plt.figure(figsize=(10, 6))
    plt.bar(iter_ls, best_energies, width = 0.5 , color = "cornflowerblue", label = "$\\epsilon(\cdot)$")
    plt.hlines(energy_mean, iter_ls[0], iter_ls[-1], color = "salmon", label = "$\hat{\\epsilon}_{best}(\cdot)$")
    plt.grid()
    plt.xlabel("iteration $i$")
    plt.ylabel("energy $\\epsilon$ / 1")
    plt.title(f'TSP with {num_cities} cities for fixed $N_s$ = {N_s} & $M$ = {M} for {iterations} iterations over different city configurations', fontsize = 12)
    plt.legend()
    plt.xticks([])
    plt.savefig(f"convergence_plot_N={num_cities}_i={iterations}.png")
    plt.show()

if __name__ == "__main__":

    iterations = 100
    num_cities = [20, 40]
    _ = [main_fixed_config(iterations, num_cities = n) for n in num_cities]
