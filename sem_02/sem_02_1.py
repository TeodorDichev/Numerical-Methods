import numpy as np
import matplotlib.pyplot as plt

# tutorial
# f_y = np.exp(f_x) as a list
# g_y = 1 + g_x + 0.5*(g_x**2) + 0.1667*(g_x**3) as a list
# plt.scatter(g_x, g_y) draws points
x = np.linspace(-2, 2, 100)
def f(x):
    return np.exp(x)

def g(x):
    return 1 + x + 0.5*(x**2) + 0.1667*(x**3)

def e_a(x):
    return f(x) - g(x)

def e_r(x):
    return (f(x)-g(x))/f(x)

# show comparison of f to g
# plt.plot(x, f(x), x, g(x))
# plt.legend('f', 'g')
# plt.title("comp")

# show absolute error
plt.plot(x, e_a(x))
plt.legend('e_a')

# show relative error
# plt.plot(x, e_r(x))
# plt.legend('e_r')

plt.show()
