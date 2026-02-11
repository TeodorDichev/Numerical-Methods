import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)

def cheb_poly(n, x):
    return np.cos(n*np.arccos(x))

for n in range(5):
    plt.plot(x, cheb_poly(n, x), label="T" + str(n) + "(x)")

plt.legend()
plt.show()