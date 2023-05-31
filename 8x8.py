import numpy as np
from ant_colony import AntColony

dist = np.array([[np.inf, 40 , 69 , 23 , np.inf, 65 , np.inf, np.inf],
                 [40 , np.inf, 46 , np.inf, np.inf, np.inf, np.inf, np.inf],
                 [69 , 46 , np.inf, np.inf, np.inf, 100, np.inf, np.inf],
                 [23 , np.inf, np.inf, np.inf, 42 , 75 , np.inf, np.inf],
                 [np.inf, np.inf, np.inf, 42 , np.inf, np.inf, np.inf, 399],
                 [65 , np.inf, 100, 75 , np.inf, np.inf, 76 , np.inf],
                 [np.inf, np.inf, np.inf, np.inf, np.inf, 76 , np.inf, 386],
                 [np.inf, np.inf, np.inf, np.inf, 399, np.inf, 386, np.inf]])

ant_colony = AntColony(dist, 10, 20, 100, 0.5, alpha=0.1, beta=1)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))
