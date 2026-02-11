import numpy as np
import matplotlib.pyplot as plt

n = 5
nodes = np.array([1,2,3,4,5])
vals = np.array([3, 55, 128, 1050, 13500])

# def basis(x):
#     return np.array([1, np.e**(x*1), np.e**(x*2), np.e**(x*3), np.e**(x*4)])

A = np.zeros([n,n])
# for i in range(n):
#     A[i] = basis(nodes[i])
    
for i in range(n):
    for j in range(n):
        A[i,j] = np.e ** (nodes[i] * j)
        
coef = np.linalg.solve(A, vals)

# def P(x):
#     return  (1 * coef[0] +
#             np.e**(x*1) * coef[1] +
#             np.e**(x*2) * coef[2] +
#             np.e**(x*3) * coef[3] +
#             np.e**(x*4) * coef[4])
    
def P(x):
    poly = 0
    for i in range(n):
        poly += coef[i] * np.e ** (i * x)
    return poly

points = np.linspace(1, 5, 100)
plt.plot(points, P(points))
plt.scatter(nodes, vals)
plt.show()