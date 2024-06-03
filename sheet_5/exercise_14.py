import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

def init_lattice(N):
    lattice_config = np.random.choice([1, -1], size = (N,N))
    return lattice_config

def delta_energy(lattice_config):
    energy = 0
    LC = lattice_config
    N = len(config)

    for i in range(N):
        for j in range(N):

            S = LC[i,j]
            nb = LC[(i + 1)%N, j] + LC[(i-1)%N, j] + LC[i, (j+1)%N] + LC[i, (j-1)%N]
            energy += -nb * S

    return energy/4

def mc_move(lattice_config, beta):
    LC = lattice_config

    for _ in range(N**2):
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
        S =  LC[i,j]

        nb = LC[(i + 1)%N, j] + LC[(i-1)%N, j] + LC[i, (j+1)%N] + LC[i, (j-1)%N]

        energy = 2*S*nb

        if energy < 0:
            S = S * (-1)
        elif rand() < np.exp(-energy * beta):
            S = S * (-1)

        LC[i, j] = S

    return LC

def magnetization(LC):
    return np.sum(LC)

def ising(time_steps, N, beta):
    lattice_config = init_lattice(N)
    M_array = np.zeros(time_steps)

    for i in range(0, time_steps):
        lattice_config = mc_move(lattice_config, beta)
        print(lattice_config)
        M = magnetization(lattice_config)
        M_array[i] = M

    return M_array, lattice_config

N = 10
T = 2.3
beta = 1/T
time_steps = 1000

M_array, LC = ising(time_steps, N, beta)

plt.title("Magnetization over MC time $\\tau$")
plt.plot(np.arange(0,time_steps,1), M_array)
plt.xlabel("$\\tau$")
plt.ylabel("<M>")
plt.show()

plt.title("Lattice configuration with spin +/- for 2D Ising Model")
plt.imshow(LC)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
