import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.2, 0.5, 0.7, 0.8, 1.0])
vals = np.array([15.7927, 35.4933, 67.5412, 95.2408, 195.334])

n = 5
A = np.zeros((n, n))

def basis(x):
    return np.array([1, np.e**x, np.e**(x*2), np.e**(x*3), np.e**(x*4)])

for i in range(n):
    A[i] = basis(x[i])

coef = np.linalg.solve(A, vals)

def P(x):
    return (coef[0]
            + coef[1]*np.e**x
            + coef[2]*np.e**(x*2)
            + coef[3]*np.e**(x*3)
            + coef[4]*np.e**(x*4))

space = np.linspace(0.15, 1.05, 300)
plt.plot(space, P(space), label="poly")
plt.scatter(x, vals, color="red")
plt.legend()
plt.show()
