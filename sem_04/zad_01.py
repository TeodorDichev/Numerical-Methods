import numpy as np
import matplotlib.pyplot as plt

def l(x):
    return 1 - x/2

def f(x):
    return 1/(1+x)

def estimate_error(x):
    return abs(x*(x-1))

x = np.linspace(0,1,100)

# function and interpolation function
plt.plot(x, f(x))
plt.plot(x, l(x))
plt.show()

# error graphs 
plt.plot(x, abs(f(x) - l(x)))
plt.plot(x, estimate_error(x))
plt.show()