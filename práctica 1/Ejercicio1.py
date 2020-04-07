# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:47:43 2020

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
    return x**3 + 4*x**2 -10
def fnum(x):
    return x**3 + 4*x**2 -10
def f(x):
    return fsym(x)

a=1.; b=2.;

sp.plot(f(x),(x,a,b))
print('Como podemos observar en el gráfico, solo tiene una raiz en el intervalo [1,2] \n\n')
sol_exact=sp.solve(f(x),x)[2]

a0=a; b0=b;

mp=10
prec=10**(-mp)

cifras=6

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

print('\n\n')
#Algoritmo de N-R

print('Algorimto de Newton-Raphson')
def df(x):
    return 3*x**2 + 8*x

x0 = Decimal(b); niter = 0;
getcontext().prec = cifras;
for k in range(nmax):
    niter = niter + 1;
    x1 = x0 - f(x0)/Decimal(df(x0))  # método de Whitaker
    #x1 = x0 - f(x0)/df(x0)   método de N-R
    # Cambiar m por Decimal(df(x0)) para el de Newton-Raphson
    if abs(x1-x0) < tol:
        sale = 'tolerancia'
        break
    if abs(f(x1)) < prec:
        sale = 'precision'
        break
    else:
        x0 = x1
                
print('sale el programa por ',sale)
if sale == 'precision':
    print('Posiblemente solución exacta: ',x1)
elif k <= nmax:
    print('Aproximación solicitada: ', x1)
else:
    print('Se llegó al número máximo de iteraciones')
print('Solución exacta con ', cifras, ' cifras significativas', sol_exact.evalf(n=cifras))
print('Número total de iteraciones ', niter)

getcontext().prec = mporig # Se restaura la precisión por defecto


































