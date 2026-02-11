import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

nodes = [0, 1.525, 3.05, 4.575, 6.1]
values = [1, 0.8617, 0.7385, 0.6292, 0.5328]

def lx(nodes, k, x):
    res = 1
    for i in range(len(nodes)):
        if i != k:
            res *= (x - nodes[i]) / (nodes[k] - nodes[i])
    return res

def L(nodes, values, x):
    res = 0
    for k in range(len(nodes)):
        res += values[k] * lx(nodes, k, x)
    return res

x_points = np.linspace(0, 6.5, 100)

plt.plot(x_points, L(nodes, values, x_points))
plt.scatter(nodes, values)
plt.show()

print(L(nodes, values, 3))