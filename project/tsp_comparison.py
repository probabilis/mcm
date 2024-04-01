import numpy as np
import matplotlib.pyplot as plt
from main import city_map, metropolis

#plt.style.use('dark_background')

def plot_path(cities, tour):
    x = [cities[i][0] for i in tour]
    y = [cities[i][1] for i in tour]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'ro-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path of the Best Tour')
    plt.grid()

    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, str(i), color= 'black', fontsize = 10, ha = 'left', va='top')

    plt.show()


def main():
    M_arr = [10, 100, 2000]
    Ns_arr = [5, 10, 100]
    
    num_cities = 10
    cities = city_map(num_cities, 0)

    beta = 0.1 ; delta_beta = 0.1

    fig, axs = plt.subplots(len(M_arr), len(Ns_arr), sharex = True, sharey = True )
    fig.set_size_inches(16, 12)
    for m, M in enumerate(M_arr):
        for n, Ns in enumerate(Ns_arr):

            best_tour, best_energy = metropolis(cities, M, Ns)

            x = [cities[i][0] for i in best_tour]
            y = [cities[i][1] for i in best_tour]
            x.append(x[0])
            y.append(y[0])


            axs[m, n].plot(x, y, linestyle = "--",marker = ".", markerfacecolor = 'white', color = np.random.rand(3,))
            axs[m, n].set_xlabel('X')
            axs[m, n].set_ylabel('Y')

            #plt.title('Path of the Best Tour')
            axs[m, n].grid()
            axs[m, n].set_title(f"$M$ = {M}, $N_s$ = {Ns} / Lowest energy (distance) $\\epsilon$ = {round(best_energy, 2)}")

            for i, (xi, yi) in enumerate(zip(x, y)):
                if i != 0:
                    axs[m, n].text(xi, yi, str(i), color= 'black', fontsize = 12, ha = 'left', va = 'top')

            del x ; del y
    
    fig.suptitle(f'Travelling salesman problem (TSP) with {num_cities} cities for different combinations of $M$ and $N_s$', fontsize=12)
    fig.tight_layout()

    plt.savefig("differnt_path_combinations_v0.png")
    plt.show()

main()