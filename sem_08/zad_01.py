import sympy as sp

a,b = sp.symbols('a, b')
def phiiiiii(a,b):
    return (b)**2 + (a+b-1)**2 + (2*a+b-1)**2 +(3*a+b-2)**2 + (4*a+b-2)**2



print(sp.solve([sp.Eq(sp.diff(phiiiiii(a,b), a), 0), sp.Eq(sp.diff(phiiiiii(a,b), b), 0)], a,b))