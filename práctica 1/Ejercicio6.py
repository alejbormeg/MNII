# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:21:09 2020

@author: Alejandro
"""


"EJERCICIO 6"

import numpy as np
import sympy as sp
from decimal import getcontext
from decimal import Decimal

from numpy import sign

def mychop(expr, *, max=10**(-10)):
    if abs(expr) > max:
      return expr 
    else:
      return 0
chop_vec = np.vectorize(mychop)

mporig = getcontext().prec

x = sp.Symbol('x')
def fsym(x):
    return x**3 - x - 1 
def f(x):
    return fsym(x)
def df(x):
    return 3*x**2 - 1 

def gNR(x):
    return x - f(x)/df(x)

a = 1.; b = 2.;
sol_exact = sp.solve(f(x),x)[2] # Solucion exacta

# x0 = 2 -> f(x0)f''(x0)>0 

mp = 5
prec = 10**(-mp)

cifras = 3

tol = 10**(-cifras)

nmax = 100


a0 = a; b0 = b;
biseccion=[];
niter = 0; getcontext().prec = cifras
for k in range(nmax):
    niter = niter + 1;
    c = (a+b)/2
    biseccion.append(c)
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

print('Metodo biseccion:')
print (biseccion)
if sale == 'precision':
    print('Posiblemente solución exacta: ',c)
elif k <= nmax:
    print('Aproximación solicitada: ',Decimal(c))
else:
    print('Se llegó al número máximo de iteraciones')
print('Número total de iteraciones ', niter)
print()
a = a0; b = b0 # Restauramos los valores originales de a y b
getcontext().prec = mporig # así como la precisión por defecto

# Aitken
aprox=biseccion          # Vector con los elementos iterados que queremos acelerar
n = len(aprox)           # Número de elementos de aprox
aitken = []              # Definición del vector de soluciones

def Aitken():
    k = 0;
    for k in range(n-2):
        aproxacel = aprox[k]-(aprox[k+1]-aprox[k])**2/(aprox[k+2]-2*aprox[k+1]+aprox[k]);
        aitken.append(aproxacel);
    print('Aceleración de Aitken:\n',aitken)
    
Aitken()

#Steffensen
aprox= biseccion       # Vector con los elementos iterados que queremos acelerar
n= len(aprox)          # Numero de iteraciones del metodo que queramos acelerar
tol= 10**(-5)          # Diferencia en valor absoluto entre una aproximación y la solución
steff= [1];            # Definición del vector de soluciones. Debe estar inicializado a algún valor para que no de errores

def g(x):              # Funcion que queremos que aplique
    return x - f(x)

def Steffensen():
    k = 0;
    while np.abs(sol_exact - steff[len(steff)-1]) > tol:
        s0 = aprox[k]-(aprox[k+1]-aprox[k])**2/(aprox[k+2]-2*aprox[k+1]+aprox[k])
        s1 = g(s0)
        s2 = g(s1)
        steff.append(s0);
        aprox.clear()
        aprox.append(s0); aprox.append(s1); aprox.append(s2)

    steff.pop(0)    
    print('Aceleración de Steffensen:\n', steff)
    
Steffensen()








print('\n\n\n Solucion por N-R:')
# xo = 2 = b

x0 = sp.N(b); maxiter = 100;
aproxNR = [x0]; niter = 0;
for k in range(maxiter):
    x1 = gNR(x0);
    aproxNR.append(x1); niter = niter + 1
    if abs(x1-x0) < tol: break
    x0 = x1
print(aproxNR)
print('N de iteraciones realizadas: ', niter)

aprox = aproxNR; 
n = len(aprox)
aitken= []
Aitken()


aprox = aproxNR; 
n = len(aprox)
tol= 10**(-5)          
steff= [1];

def g(x):
    return x-f(x)

Steffensen()




