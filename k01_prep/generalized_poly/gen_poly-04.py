import numpy as np
import matplotlib.pyplot as plt

n = 6
nodes = [0, 0.03,0.07,0.15,0.21,0.27]
values = [1,1.06,2.09,22.1,99.78,328.602]
A = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i,j] = np.e ** (nodes[i] * j)

coef = np.linalg.solve(A, values)

def P(x):
    poly = 0
    for i in range(n):
        poly += coef[i] * np.e ** (i * x)
    return poly

points = np.linspace(0, 0.3, 199)
plt.plot(points, P(points))
plt.scatter(nodes, values)
plt.show()

