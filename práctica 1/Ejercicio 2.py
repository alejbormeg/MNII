# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:25:07 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp
from decimal import getcontext
from decimal import Decimal
from numpy import sign

def mychop(expr, *, max=10**(-10)):
    ''' Esta función redondea por cero cualquier número más
    pequeño a la cantidad máxima indicada'''
    if abs(expr) > max:
      return expr 
    else:
      return 0
chop_vec = np.vectorize(mychop)
mporig=getcontext().prec

x=sp.Symbol('x')
def fsym(x):
    return x**3 - 25
def fnum(x):
    return x**3 - 25
def f(x):
    return fsym(x)

a=0.; b=4.;

sp.plot(f(x),(x,a,b))
sol_exact=sp.solve(f(x),x)[0]

print('Solucion exacta: ', sol_exact)
a0=a; b0=b;

mp=10
prec=10**(-mp)

cifras=3

tol=10**(-cifras)

nmax=150
#Algoritmo de bisección
print('Algoritmo de Bisección')
niter = 0; getcontext().prec = cifras
for k in range(nmax):
    niter = niter + 1;
    c = a + (b-a)/2 # equivalente a c = (a+b)/2
    if abs(f(c)) < prec:
        sale = 'precision'
        break
    if sign(f(a)) != sign(f(c)):
        b = c
    else:
        a = c
    if b-a < tol:
        sale = 'tolerancia'
        break

if sale == 'precision':
    print('Posiblemente solución exacta: ',c)
elif k <= nmax:
    print('Aproximación solicitada: ',Decimal(c))
else:
    print('Se llegó al número máximo de iteraciones')
print('Solución exacta con ', cifras, ' cifras significativas', sol_exact.evalf(n=cifras))
print('Número total de iteraciones ', niter)

a = a0; b = b0 # Restauramos los valores originales de a y b
getcontext().prec = mporig # así como la precisión por defecto




