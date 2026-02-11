import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8])
vals = np.array([0.1, 0.009, 0.0011, 0.00003, 0.0000012])

n = 5
A = np.zeros((n, n))

# def basis(x):
#     return np.array([1, 1/(1+x), 1/(2+x), 1/(3+x), 1/(4+x)])

# for i in range(n):
#     A[i] = basis(x[i])
    
# second way to fill:
for i in range(n):
    A[i,0] = 1
    for j in range(1, n):
        A[i,j] = 1/(j + x[i])

coef = np.linalg.solve(A, vals)

# def P(x):
#     return (coef[0]
#             + coef[1]*(1/(1+x))
#             + coef[2]*(1/(2+x))
#             + coef[3]*(1/(3+x))
#             + coef[4]*(1/(4+x)))
    
def P(x):
    poly = coef[0]
    for i in range(1, n):
        poly += coef[i] * (1/(i + x))
        
    return poly

space = np.linspace(0, 8, 300)
plt.plot(space, P(space), label="poly")
plt.scatter(x, vals, color="red")
plt.legend()
plt.show()
