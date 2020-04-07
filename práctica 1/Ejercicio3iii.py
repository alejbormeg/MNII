# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:36:37 2020

@author: Alejandro
"""
import numpy as np
import sympy as sp
import math
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

print ('Ejercicio 3 iii)')


x=sp.Symbol('x')
def fsym(x):
    return x**2 +10*sp.cos(x) + x
def fnum(x):
    return x**2 +10*sp.cos(x) + x
def f(x):
    return fsym(x)

a=-5.; b=5.;

sp.plot(f(x),(x,a,b))
print('Como podemos observar en el gráfico, tiene dos raices en el intervalo [-5,5] para aproximar la primera y aplicaremos N-R en [-5,-3] y en [-2,0] \n\n')

mp=10
prec=10**(-mp)

cifras=5

tol=10**(-cifras)

nmax=150

def df(x):
    return 2*x +1 +10*(-sp.sin(x))

print ('Veamos la primera raiz')
a1=-5. ; b1=-3.;
sp.plot(f(x),(x,a1,b1))

x0 = Decimal(a1); niter = 0;
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

print ('Veamos la primera raiz')
a1=-2. ; b1=0.;
sp.plot(f(x),(x,a1,b1))

x0 = Decimal(a1); niter = 0;
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


