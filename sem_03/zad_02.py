import numpy as np
import matplotlib.pyplot as plt
import sympy

# Nodes
x0 = 0
x1 = np.pi/6
x2 = np.pi/3
x3 = np.pi/2

# Lagrange basis polynomials
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

# prints the interpolated polynomial by symbols
x = sympy.symbols('x')
print(sympy.expand(y(x)))

# True function
def y_true(x):
    return np.sin(x)

# Plot range
space = np.linspace(0, np.pi, 200)

plt.plot(space, y_true(space), label='sin(x)')
plt.plot(space, y(space), '--', label='Lagrange interpolation')
plt.scatter([x0, x1, x2, x3],
            [np.sin(x0), np.sin(x1), np.sin(x2), np.sin(x3)],
            color='red', label='Nodes')
plt.legend()
plt.show()

# Comparison at x = π/5
print("Interpolated:", y(np.pi/5))
print("True value  :", y_true(np.pi/5))



