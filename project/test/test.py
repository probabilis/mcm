import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt

def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

def total_distance(tour, cities):
    total = 0
    for i in range(len(tour)):
        total += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return total

def initial_tour(num_cities):
    return list(range(num_cities))

def swap(tour):
    new_tour = tour.copy()
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def metropolis_hastings(cities, temperature, cooling_rate, M, Ns):
    current_tour = initial_tour(len(cities))
    current_energy = total_distance(current_tour, cities)
    print('Current Energy: ', current_energy)


    best_tour = current_tour
    best_energy = current_energy

    for _ in range(M):

        proposed_tour = swap(current_tour)
        proposed_energy = total_distance(proposed_tour, cities)

        for _ in range(Ns):

            if proposed_energy < current_energy or random.random() < math.exp((current_energy - proposed_energy) / temperature):
                current_tour = proposed_tour
                current_energy = proposed_energy

            if current_energy < best_energy:
                best_tour = current_tour
                best_energy = current_energy

            temperature *= cooling_rate

    return best_tour, best_energy

def plot_path(cities, tour):
    x = [cities[i][0] for i in tour]
    y = [cities[i][1] for i in tour]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'ro-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path of the Best Tour')

    # Add numeration
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, str(i), color="blue", fontsize=12, ha='center', va='center')

    plt.show()

if __name__ == "__main__":
    st = time.time()
    np.random.seed(0) 
    num_cities = 10
    cities = np.random.rand(num_cities, 2)

    initial_temperature = 1000
    cooling_rate = 0.995
    M = 10000
    Ns = 1

    best_tour, best_energy = metropolis_hastings(cities, initial_temperature, cooling_rate, M, Ns)

    print("Best tour:", best_tour)
    print("Best energy:", best_energy)
    et = time.time()
    print("Time needed for calculation: %.2f seconds." %(et-st) )

    plot_path(cities, best_tour)