import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def div_diff(nodes, values):
    n = len(nodes)
    if n == 1:
        return values[0]
    
    return (div_diff(nodes[1:n], values[1:n]) - div_diff(nodes[0:n-1], values[0:n-1])) / (nodes[n-1] - nodes[0])

def newton_poly(x, nodes, values):
    n = len(nodes)
    poly = 0
    prod = 1
    # with poly and prod you can do it with one for
    for i in range(n):
        poly += div_diff(nodes[0:i+1], values[0:i+1]) * prod
        prod *= (x - nodes[i])
    
    return poly

points = np.linspace(1,5,100)
plt.plot(points, newton_poly(points, [3,4], [7,3]), label="f1")
plt.plot(points, newton_poly(points, [2.5,3,4], [6.5,7,3]), label="f2")
plt.plot(points, newton_poly(points, [2,3.5,3,4], [5,6.5,7,3]), label="f3")
plt.scatter([2,3.5,3,4], [5,6.5,7,3])
plt.legend()
plt.show()

print("F1(3.4): " + "{0:.3f}".format(newton_poly(3.4, [3,4], [7,3])))
print("F2(3.4): " + "{0:.3f}".format(newton_poly(3.4, [2.5,3,4], [6.5,7,3])))
print("F3(3.4): " + "{0:.3f}".format(newton_poly(3.4, [2,3.5,3,4], [5,6.5,7,3])))