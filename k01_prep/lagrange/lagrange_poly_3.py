import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def f(x):
    return np.e**x

nodes = [0, 0.1, 0.2, 0.3]
values = [1, 1.10517, 1.2214, 1.34986]

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

# ako ne e dadena tablica polzvai f(x) vmesto values
# def L(nodes, f, x):
#     res = 0
#     for k in range(len(nodes)):
#         res += f(x) * lx(nodes, k, x)
#     return res

points = np.linspace(0, 0.3, 100)

plt.plot(points, f(points), label='func')
plt.plot(points, L(nodes, values, points), label='lagrange')
plt.legend()
plt.show()

def abs_err(x):
    return abs(f(x) - L(nodes, values, x))

def est_err(nodes, x):
    res = np.exp(0.3)/24
    for i in range(len(nodes)):
        res *= (x - nodes[i])
    return abs(res)

plt.plot(points, abs_err(points), label='abs')
plt.plot(points, est_err(nodes, points), label='est')
plt.legend()
plt.show()

print(L(nodes, values, 0.15))