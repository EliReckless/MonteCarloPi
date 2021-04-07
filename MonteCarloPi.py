import numpy as np
import matplotlib.pyplot as plt

n=10000

while n < 1000000:
    x = np.random.rand(n,2)
    inside = x[np.sqrt(x[:,0]**2+x[:,1]**2) < 1]
    estimate = 4*len(inside)/len(x)
    print("Schätzung von Pi bei {}: {}".format(n, estimate))

    plt.figure(figsize=(6,6))
    plt.scatter(x[:,0], x[:,1], s=.00002, c="green")
    plt.scatter(inside[:,0], inside[:,1], s=.00002, c="red")
    plt.savefig("MonteCarloPi{}.png".format(n))
    
    n += 10000