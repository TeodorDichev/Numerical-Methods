import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def p(x):
    return (x-2)**9

def p_expanded(x):
    # x=sp.symbols('x') can print than copy instead of just write
    return x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

x = np.linspace(1.92, 2.05, 1000)
# show comparison of f to g
plt.plot(x, p(x), x, p_expanded(x))
plt.legend('p', 'p_expanded')
plt.title("comp")

plt.show()
