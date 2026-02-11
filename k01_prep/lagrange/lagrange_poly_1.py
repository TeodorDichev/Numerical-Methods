import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

nodes = [0, 0.5, 1, 1.5]
values = [1, 2, 3, 4]

def lx (nodes, k, x):
    res = 1
    for i in range(len(nodes)):
        if i != k:
            res *= (x - nodes[i]) / (nodes[k] - nodes[i])
    return res

def L (values, nodes, x):
    res = 0
    for k in range(len(nodes)):
        res += values[k] * lx(nodes, k, x)
    return res

x_points = np.linspace(0, 1.5, 100)

plt.plot(x_points, L(values, nodes, x_points))
plt.show()

x = sp.symbols('x')
print(sp.expand(L(values, nodes, x)))