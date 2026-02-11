import sympy
import numpy
import matplotlib.pyplot as plt

def f(x):
    return sympy.exp(x)

def p(a,b,c,x):
    return a*x**2 + b*x + c

# Symbolic expansion
x,a,b,c = sympy.Symbol('x'),sympy.Symbol('a'),sympy.Symbol('b'),sympy.Symbol('c')

def phi(a,b,c,x):
    return sympy.integrate(1 * (f(x) - p(a,b,c,x))**2, (x, 0, 1.5))

sol = sympy.solve([sympy.diff(phi(a,b,c,x), a), 
                  sympy.diff(phi(a,b,c,x), b), 
                  sympy.diff(phi(a,b,c,x), c)], [a,b,c])

# print(sol)

space = numpy.linspace(0, 1.5, 100)

f_num = sympy.lambdify(x, f(x), "numpy")
p_num = sympy.lambdify(x, p(sol[a], sol[b], sol[c], x), "numpy")

plt.plot(space, f_num(space))
plt.plot(space, p_num(space))
plt.show()