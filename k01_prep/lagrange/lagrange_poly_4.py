import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# -------------------------
# Lagrange interpolation
# -------------------------

def l(nodes, k, x):
    prod = 1
    for i in range(len(nodes)):
        if i != k:
            prod *= (x - nodes[i]) / (nodes[k] - nodes[i])
    return prod

def lagrange_poly(n, x0, h, f, x):
    nodes = [x0 + i * h for i in range(n + 1)]
    poly = 0
    for k in range(n + 1):
        poly += f(nodes[k]) * l(nodes, k, x)
    return poly

# -------------------------
# Example parameters
# -------------------------

n = 3
x0 = 0
h = 1

# function
def f(x): return np.sin(x)

# symbolic variable
xs = sp.symbols("x")

# symbolic polynomial
poly_sym = lagrange_poly(n, x0, h, sp.sin, xs)
poly_expanded = sp.expand(poly_sym)

print("Expanded polynomial:")
print(poly_expanded)

# -------------------------
# Plot
# -------------------------

x_points = np.linspace(0, 3, 200)

plt.plot(x_points, f(x_points), label="sin(x)")
plt.plot(x_points, lagrange_poly(n, x0, h, f, x_points), label="Lagrange poly (n=3)")
plt.scatter([x0 + i*h for i in range(n+1)],
            [f(x0 + i*h) for i in range(n+1)])

plt.legend()
plt.show()
