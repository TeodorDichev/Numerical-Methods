import numpy as np
import matplotlib.pyplot as plt

def Lagrange(n, A, B, f, x):
    step = (B - A) / n
    nodes = [A + k * step for k in range(n + 1)]

    poly = 0
    for i in range(n + 1):
        xi = nodes[i]
        li = 1
        for j in range(n + 1):
            if j != i:
                li *= (x - nodes[j]) / (xi - nodes[j])
        poly += f(xi) * li

    return poly

def f(x):
    return np.sin(x)

n = 5
A = 0
B = np.pi

xs = np.linspace(A - 0.5, B + 0.5, 400)
ys_true = f(xs)
ys_interp = [Lagrange(n, A, B, f, xx) for xx in xs]

plt.plot(xs, ys_true, label="sin(x)")
plt.plot(xs, ys_interp, label="Lagrange (n=5)")
plt.scatter([A + k*(B-A)/n for k in range(n+1)],
            [f(A + k*(B-A)/n) for k in range(n+1)],
            color="red", label="nodes")

plt.legend()
plt.show()
