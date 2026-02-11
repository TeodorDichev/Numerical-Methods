import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

nodes = np.array([0, 1, 4])
values = np.array([2, 5, 48])

def f(x):
    return np.sqrt(x) + 3*x**2 - x + 2

# Recursive divided difference
def div_diff(nodes, values):
    if len(nodes) == 1:
        return values[0]
    #      from 1 to n - 1                    from 0 to n - 2                         n - 1         
    return (div_diff(nodes[1:], values[1:]) - div_diff(nodes[0:-1], values[0:-1])) / (nodes[-1] - nodes[0])

# Recursive divided difference
def div_diff_1(nodes, values):
    n = len(nodes)
    if n == 1:
        return values[0]
    #      from 1 to n - 1                    from 0 to n - 2                         n - 1         
    return (div_diff_1(nodes[1:n], values[1:n]) - div_diff_1(nodes[0:n-1], values[0:n-1])) / (nodes[n-1] - nodes[0])


# Build Newton polynomial
def newton_poly(nodes, values, x):
    n = len(nodes)
    res = 0
    for i in range(n):
        term = div_diff(nodes[0:i+1], values[0:i+1])
        for j in range(i):
            term *= (x - nodes[j])
        res += term
    return res

# Build Newton polynomial
def newton_poly_1(nodes, values, x):
    n = len(nodes)
    poly = 0
    prod = 1
    for i in range(n):
        poly += div_diff(nodes[0:i+1], values[0:i+1]) * prod
        prod *= (x - nodes[i])
        
    return poly

# Numeric plot
x_vals = np.linspace(0, 4, 200)
plt.plot(x_vals, f(x_vals), label="f(x)")
plt.plot(x_vals, newton_poly(nodes, values, x_vals), label="Newton interp.")
plt.legend()
plt.show()

# Symbolic expansion
x = sp.Symbol('x')
poly_expr = newton_poly(nodes, values, x)
print(sp.expand(poly_expr))
