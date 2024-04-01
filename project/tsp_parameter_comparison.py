import numpy as np
import matplotlib.pyplot as plt
from main import city_map, metropolis

#calculate mean and variance of best_energy for different M

def main_M():
    M_ls = [5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    Ns = 100
    
    num_cities = 10
    cities = city_map(num_cities)

    best_energies = []

    for M in M_ls:
        best_tour, best_energy = metropolis(cities, M, Ns)
        best_energies.append(best_energy)
    

    M_ls = [str(m) for m in M_ls]
    energy_mean = np.mean(best_energies)
    energy_var = np.var(best_energies)
    print(f"The best energy average is: {energy_mean} and variance is: {energy_var}")
    plt.figure(figsize=(10, 6))
    plt.bar(M_ls, best_energies, width = 0.5 , color = "gray")
    plt.grid()
    plt.xlabel("$M$")
    plt.ylabel("energy $\\epsilon$ / 1")
    plt.title(f'TSP with {num_cities} cities for different combinations of $M$ with fixed $N_s$ = {Ns}', fontsize=12)
    plt.savefig("convergence_plot_over_different_M_random.png")
    plt.show()

main_M()

#calculate mean and variance of best_energy for different Ns

def main_Ns():
    Ns_ls = [5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    M = 100
    
    num_cities = 10
    cities = city_map(num_cities)

    best_energies = []

    for Ns in Ns_ls:
        best_tour, best_energy = metropolis(cities, M, Ns)
        best_energies.append(best_energy)
    
    Ns_ls = [str(m) for m in Ns_ls]

    energy_mean = np.mean(best_energies)
    energy_var = np.var(best_energies)
    print(f"The best energy average is: {energy_mean} and variance is: {energy_var}")

    plt.figure(figsize=(10, 6))
    plt.bar(Ns_ls, best_energies, width = 0.5 , color = "gray")
    plt.grid()
    plt.xlabel("$N_s$")
    plt.ylabel("energy $\\epsilon$ / 1")
    plt.title(f'TSP with {num_cities} cities for different combinations of $N_s$ with fixed $M$ = {M}', fontsize=12)
    plt.savefig("convergence_plot_over_different_Ns_random.png")
    plt.show()

main_Ns()