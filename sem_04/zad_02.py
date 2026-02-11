import numpy as np
import matplotlib.pyplot as plt

# estimating error for zad_02 and zad_01 (sin and interpol pol for sin)
x0 = 0
x1 = np.pi/6
x2 = np.pi/3
x3 = np.pi/2

def est_err(x):
    return 1/24*abs(x*(x - x1)*(x - x2)*(x - x3))

def L0(x):
    return ((x - x1)*(x - x2)*(x - x3)) / ((x0 - x1)*(x0 - x2)*(x0 - x3))

def L1(x):
    return ((x - x0)*(x - x2)*(x - x3)) / ((x1 - x0)*(x1 - x2)*(x1 - x3))

def L2(x):
    return ((x - x0)*(x - x1)*(x - x3)) / ((x2 - x0)*(x2 - x1)*(x2 - x3))

def L3(x):
    return ((x - x0)*(x - x1)*(x - x2)) / ((x3 - x0)*(x3 - x1)*(x3 - x2))

# Interpolated polynomial
def y(x):
    return (np.sin(x0)*L0(x) +
            np.sin(x1)*L1(x) +
            np.sin(x2)*L2(x) +
            np.sin(x3)*L3(x))

# same as y
def y_pol(x):
    return -0.113871899071412*x**3 - 0.0654708032116345*x**2 + 1.02042871862363*x

# True function
def y_true(x):
    return np.sin(x)

# Plot range
space = np.linspace(0, np.pi/2, 100)

# error graphs 
plt.plot(space, abs(y_true(space) - y(space)))
plt.plot(space, est_err(space))
plt.show()