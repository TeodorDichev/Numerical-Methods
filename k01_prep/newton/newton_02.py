import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

nodes = np.array([0, np.pi/4, np.pi/2])

def f(x):
    return np.cos(x)

def div_diff(nodes):
    n = len(nodes)
    if n == 1:
        return f(nodes[0])
    
    return (div_diff(nodes[1:n]) - div_diff(nodes[0:n-1]))/(nodes[n-1]-nodes[0])

def newton_interpol(nodes, x):
    n = len(nodes)
    poly = 0
    prod = 1

    for i in range(n):
        poly += div_diff(nodes[0:i+1]) * prod
        prod *= (x-nodes[i])

    return poly

# calculated on hand
def ermit(x):
    return 1 + ((-4)/(np.pi**2))*(x**2)

points = np.linspace(0, np.pi/2, 100)
plt.plot(points, f(points), label="cos")
plt.plot(points, newton_interpol(nodes, points), label="newton")
plt.plot(points, ermit(points), label="ermit")
plt.scatter(nodes, f(nodes))
plt.legend()
plt.show()

# delenie na 0 ??
# def Rx_newton(x):
#     return (abs(f(x) - newton_interpol(nodes, x))) # ? /f(x)

# def Rx_ermit(x):
#     return (abs(f(x) - ermit(x)))# ? /f(x)


# from chat
def Rx_newton(x):
    return abs(f(x) - newton_interpol(nodes, x)) / abs(f(x))

def Rx_ermit(x):
    return abs(f(x) - ermit(x)) / abs(f(x))

# exclude f(x)=0 to avoid division by zero
mask = abs(f(points)) > 1e-12
points_safe = points[mask]

plt.plot(points_safe, Rx_newton(points_safe), label="Newton rel err")
plt.plot(points_safe, Rx_ermit(points_safe), label="Hermite rel err")
plt.legend()
plt.show()
