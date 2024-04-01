import sys
import numpy as np

class grid_2d_cities():
    """
    Put cities on random integer vertices of [0, ncities-1] x [0, ncities-1]
    grid by default. You may also pass xlength and ylength. Each city has a
    unique vertex.
    """

    # If there are more than 9 cities, the brute force algorithm becomes too
    # slow. For n cities, we search (n-1)! routes.
    maxBruteN = 9

    def __init__(self, *args):
        if len(args) == 0:
            print('Must pass at least one integer to constructor. Exiting.')
            sys.exit()

        self.ncities = int(np.ceil(args[0]))
        self.xlength = self.ylength = self.ncities
        if len(args) > 1:
            self.xlength = int(np.ceil(args[1]))
        if len(args) > 2:
            self.ylength = int(np.ceil(args[2]))

        # Array to store coordinate pairs
        self.coords = []
        # Array to store brute force shortest route
        self.bruteshortest = []
        self.generateCities()

    def generateCities(self):
        """
        Put ncities on a [0, xlength-1] x [0, ylength-1] integer grid.
        """
        if self.ncities > self.xlength*self.ylength:
            print('The product xlength*ylength must be greather than ncities.')
            print('Cities won\'t generate until this happens.')
        else:
            for i in range(self.ncities):
                xval = int(np.floor(np.random.uniform(0,self.xlength)))
                yval = int(np.floor(np.random.uniform(0,self.ylength)))
                # Enure point is unique
                if (xval,yval) in self.coords:
                    while (xval,yval) in self.coords:
                        xval = int(np.floor(np.random.uniform(0,self.xlength)))
                        yval = int(np.floor(np.random.uniform(0,self.ylength)))
                # Add point to coordinate array
                self.coords.append((xval,yval))


cities = grid_2d_cities(9,15,15).ncities
cities = grid_2d_cities(9,15,15).coords
print(cities)