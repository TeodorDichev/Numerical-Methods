import numpy as np
import matplotlib.pyplot as plt

# Define function
def f(x):
    return np.sin(x)

# Nodes
nodes = [0, np.pi/6, np.pi/3, np.pi/2]

# Lagrange basis polynomial
def l(nodes, k, x):
    res = 1
    for i in range(len(nodes)):
        if i != k:
            res *= (x - nodes[i]) / (nodes[k] - nodes[i])
    return res

# Lagrange interpolation polynomial
def Lagrange_poly(f, nodes, x):
    res = 0
    for k in range(len(nodes)):
        res += f(nodes[k]) * l(nodes, k, x)
    return res

# Plot
points = np.linspace(0, np.pi, 120)

plt.plot(points, f(points), label='sin(x)')
plt.plot(points, Lagrange_poly(f, nodes, points), '--', label='Lagrange interpolation')
plt.scatter(nodes, f(nodes), color='red', label='Nodes')
plt.legend()
plt.show()
