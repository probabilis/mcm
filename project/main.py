"""
MCM Travelling Salesman Project
"""
import numpy as np
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('dark_background')

def city_map(num_cities, seed_ = None): 
    """
    function for assigning the city map of the TSP via random numbers sampled
    from a uniform distribution with values from x in [0,1] with number of cities from the input parameter
    """
    if num_cities <= 3:
        print("Error. Number of cities must be greater than 3.")

    if seed_ != None:
        np.random.seed(seed_)
    cities = np.random.rand( num_cities, 2 )
    return cities

def metric(city_i, city_j):
    """
    function for calculating the distance between 2 cities with the classical 
    euclidien distance metric in 2-dimenionsal plane
    """
    xi, yi = city_i[0], city_i[1]
    xj, yj = city_j[0], city_j[1] 
    return np.sqrt( (xi - xj)**2 + (yi - yj)**2 )

def matrix_assignment(cities):
    """
    function for assigning the individual distance between all cities in the map with
    the corresponding metric
    """
    num_cities = len(cities)
    d = np.zeros( (num_cities, num_cities) )

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            
            distance = metric(cities[i], cities[j])
            d[i][j] = distance
            d[j][i] = distance
    return d


def total_distance(tour, d):
    """
    function for calculating the total distance of a given route from the distance matrix d via 
    a given tour 
    """
    total_distance = 0

    for i in range(len(tour)):
        total_distance += d[ tour[i] ][ tour[ (i+1) % len(tour) ] ]

    return total_distance


def tour_swapping(tour):
    """
    function for swapping the inital tour via random integers sampled from a 
    uniform distribution
    """
    proposed_tour = tour.copy()
    i, j = random.randint(0, len(tour) - 1), random.randint(0, len(tour) - 1)
    proposed_tour[i], proposed_tour[j] = proposed_tour[j], proposed_tour[i]
    return proposed_tour


def metropolis(cities, M, Ns):
    """
    function for the Metropolis algorithm with Simulated Annealing
    """
    d = matrix_assignment(cities)

    #beta min and max are determined through beta = 1 / (k_B * T) with k_B = 1.380649 * 10E-23 m2 kg s-2 K-1
    # for very small and big temperature T
    beta_min = 10E+10 ; beta_max = 10E+100

    delta_beta = (beta_max - beta_min) / M
    beta = beta_min

    #initializing first tour in sequential order
    current_tour = list(range(len(cities)))
    #calculating the trivial energy of first tour
    current_energy = total_distance(current_tour, d)
    print('First trivial Energy is %.2f ' % current_energy)

    best_tour, best_energy = current_tour, current_energy

    for _ in range(M):
        #proposing a new tour based on a random change of two cities
        proposed_tour = tour_swapping(current_tour)
        #calculating the corresponding energy
        proposed_energy = total_distance(proposed_tour, d)

        for _ in range(Ns):
            #calculating boltzman factor through energy (action) difference between 
            #current and proposed energy
            boltzman_factor = np.exp((current_energy - proposed_energy) * beta)

            try:
                #calculating the acceptance probability and accept it if one of those conditions is true
                #1) delta_E < 0
                #2) uniform distributed sample x < boltzman_factor
                delta_E = proposed_energy - current_energy
                if delta_E < 0 or random.random() < boltzman_factor:
                    current_tour = proposed_tour
                    current_energy = proposed_energy

                #if updated current_energy < best_energy, the new best tour and best energy will be updated
                if current_energy < best_energy:
                    best_tour = current_tour
                    best_energy = current_energy
            

            except OverflowError:
                print("Overflow Error")
                pass

        #update current beta (inverse temperature) with stepsize delta_beta
        beta += delta_beta
        #print("Beta: ", beta)

    return best_tour, best_energy

def plot_path(cities, tour, color, color_font, index, label):
    allign_ha = ['left', 'right']
    allign_va = ['top', 'bottom']
    plot_style = [color + 'o-', color + 'o--']
    x = [cities[i][0] for i in tour]
    y = [cities[i][1] for i in tour]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, plot_style[index], label = label)
    plt.xlabel('X')
    plt.ylabel('Y')
    for i, (xi, yi) in enumerate(zip(x, y)):
        if i != 0:
            plt.text(xi, yi, str(i), color = color_font, fontsize = 16, ha = allign_ha[index], va = allign_va[index])


#############################################

if __name__ == "__main__":
    num_cities = 10
    seed = 0
    st = time.time()
    cities = city_map(num_cities, seed)

    M = 100 ; Ns = 100

    initial_tour = list(range(len(cities)))
    d = matrix_assignment(cities)
    initial_energy = total_distance(initial_tour, d)

    best_tour, best_energy = metropolis(cities, M, Ns)

    print("Initial tour: ", initial_tour)
    print("Initial energy: %0.3f" % initial_energy)
    print("Best tour: ", best_tour)
    print("Best energy: %0.3f" % best_energy)
    et = time.time()
    print("Time needed for calculation: %.4f seconds." %(et-st) )

    plt.figure(figsize=(10, 6))
    plot_path(cities, initial_tour[:-1], 'r', 'darkred' , 0, "initial tour")
    plot_path(cities, best_tour[:-1], 'c', 'darkblue' , 1, "best tour")
    plt.grid()
    plt.title(f'Paths of the initial and best Tour of a City Map with $N$ = {num_cities} cities / seed $s$ = {seed}')
    plt.legend()
    #plt.savefig("path_initial_best_tour_comparison_add.png")
    plt.show()
