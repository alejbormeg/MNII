# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:40:49 2020

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

print ('Ejercicio 3 i)')


x=sp.Symbol('x')
def fsym(x):
    return x**3 -x -1
def fnum(x):
    return x**3 -x -1
def f(x):
    return fsym(x)

a=1.; b=2.;

sp.plot(f(x),(x,a,b))
print('Como podemos observar en el gráfico, solo tiene una raiz en el intervalo [1,2] \n\n')
sol_exact=sp.solve(f(x),x)[2]

print('Solucion: ',sol_exact)

mp=10
prec=10**(-mp)

cifras=5

tol=10**(-cifras)

nmax=150

def df(x):
    return 3*x**2 -1

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





