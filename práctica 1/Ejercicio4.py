# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:08:09 2020

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
    return 3*x**2 + sp.exp(x) -1

def f(x):
    return fsym(x)

a=0.; b=1.;

sp.plot(f(x),(x,a,b))

a0=a; b0=b;

mp=10
prec=10**(-mp)

cifras=5

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
print('Número total de iteraciones ', niter)

a = a0; b = b0 # Restauramos los valores originales de a y b
getcontext().prec = mporig # así como la precisión por defecto

tol=10**(-4)

print ('\n\n Algoritmo N-R')
a1=0. ; b1=1.;
def df(x):
    return 6*x+sp.exp(x)
def df2(x):
    return 6 +sp.exp(x)
def gNR(x):
    return x - f(x)/df(x)
print(f(b1)*df2(b1))
print("f(x0)*f''(x0) >0, por tanto tenemos convergencia")

x0 = sp.N(b1); maxiter = 100;
aproxNR = [x0]; niter = 0;
for k in range(maxiter):
    x1 = gNR(x0);
    aproxNR.append(x1); niter = niter + 1
    if abs(x1-x0) < tol: break
    x0 = x1
print(aproxNR)


