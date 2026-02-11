import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*np.log(x)

def p(x):
    return 15*x + 3*np.log(0.2) - 3 + 150*(2*(np.log(0.3) - np.log(0.2)) - 1)*(x-0.2)**2

def R(x):
    return abs((f(x) - p(x)) / f(x))

points = np.linspace(0.2, 0.3, 100)

plt.plot(points, R(points))
plt.show()