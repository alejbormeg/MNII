# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:53:41 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp
from decimal import getcontext
from decimal import Decimal

def mychop(expr, *, max=10**(-10)):
    ''' Esta función redondea por cero cualquier número más
    pequeño a la cantidad máxima indicada'''
    if abs(expr) > max:
      return expr 
    else:
      return 0
chop_vec = np.vectorize(mychop)
mporig=getcontext().prec

print ('Ejercicio 3 ii)')


x=sp.Symbol('x')
def fsym(x):
    return x**2 +2 - sp.exp(x) -3*x
def fnum(x):
    return x**2 -3*x +2 - sp.exp(x)
def f(x):
    return fsym(x)

a=-1.; b=1.;

sp.plot(f(x),(x,a,b))
print('Como podemos observar en el gráfico, solo tiene una raiz en el intervalo [1,2] \n\n')

mp=10
prec=10**(-mp)

cifras=5

tol=10**(-cifras)

nmax=150

def df(x):
    return 2*x -3 - sp.exp(x)

print('\n\n Solución con N-R')
print('Dado que la primera derivada de f es negativa en el intervalo y la segunda deerivada positiva viendo la gráfica, tomamos x0=-1')
x0 = Decimal(a); niter = 0;
getcontext().prec = cifras;
for k in range(nmax):
    niter = niter + 1;
    x1 = x0 - f(x0)/df(x0)  # método de Whitaker
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
print('Número total de iteraciones ', niter)

getcontext().prec = mporig # Se restaura la precisión por defecto





