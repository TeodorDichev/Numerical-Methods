import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# we need a polynomial from 3rd degree => we want 4 nodes!!!
n = 4 # nodes
chebishev_nodes = np.array([np.cos((np.pi * (2*i - 1)) / (2 * n)) for i in range(1, n+1)])

def f(x):
    return np.log(x + 2)

# the problem coulc be solve with both lagrange and newton formula
# we will do newton because i have solved only 1 task with it yet
def div_diff(nodes):
    n = len(nodes)
    if n == 1:
        return f(nodes[0])
    
    return (div_diff(nodes[1:n]) - div_diff(nodes[0:n-1])) / (nodes[n-1] - nodes[0])

def newton_poly(x, nodes):
    n = len(nodes)
    poly = 0
    prod = 1

    for i in range(n):
        poly += div_diff(nodes[0:i+1]) * prod
        prod *= x - nodes[i]

    return poly

def Rx(x, nodes):
    return abs(f(x) - newton_poly(x, nodes))

nodes = np.array([-1, -0.3, 0.3, 1])
points = np.linspace(-1.1, 1.1, 100)
plt.plot(points, newton_poly(points, nodes), label="simple")
plt.plot(points, newton_poly(points, chebishev_nodes), label="chebishev")
plt.scatter(nodes, f(nodes))
plt.legend()
plt.show()

plt.plot(points, Rx(points, nodes), label="simple err")
plt.plot(points, Rx(points, chebishev_nodes), label="chebishev err")
plt.legend()
plt.show()