# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:53:52 2020

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
"Multiplicidad"
m=2
def fsym(x):
    return (x-1)*(x-3)**m

def f(x):
    return fsym(x)

def df(x):
    return (x-3)*(3*x-5)

def gNR(x):
    '''función de punto fijo asociada al método de N-R para f(x)'''
    return x - f(x)/df(x)

print ('Solución con N-R clásico')
a=2.0; b=4.0; 
x0 = sp.N(b); aproxNR = [x0]; niter = 10;
for k in range(niter):
    x1 = gNR(x0); x0 = x1
    aproxNR.append(x1)
print(aproxNR)

def gNRA(x):
        return x- m*f(x)/df(x)
    
x0 = sp.N(b); aproxNR = [x0]; niter = 10;
print ('\nSolución con N-R acelerando la convergencia')
for k in range(niter):
    x1 = gNRA(x0); x0 = x1
    aproxNR.append(x1)
print(aproxNR)


# Aitken
aprox=aproxNR          # Vector con los elementos iterados que queremos acelerar
n = len(aprox)           # Número de elementos de aprox
aitken = []              # Definición del vector de soluciones

print('\nAceleraciones de Aitken y Steffensen \n \n')

x0=sp.N(b);
Aitken =[];Steff = []; 
x1=gNR(x0); x2=gNR(x1);
a0=x0 - (x1-x0)**2/(x2-2*x1+x0);
s0=a0;
Aitken.append(a0);Steff.append(s0);

#Transcribo el código de octave de los apuntes
for k in range(niter):
    for j in range(2):
        x0=x1;x1=x2;x2=gNR(x1);
        a0=x0 - (x1-x0)**2/(x2-2*x1+x0);
        Aitken.append(a0);
        
    x0=x1;x1=x2;x2=gNR(x1);
    a0=x0 - (x1-x0)**2/(x2-2*x1+x0);
    s1 = gNR(s0); s2 = gNR(s1)
    s0 = s0 - (s1-s0)**2/(s2-2*s1+s0)
    Steff.append(s0);
    
print ('\n\nAceleracion con Aiken\n')
print(Aitken)

print ('\n\n Aceleracion con Steffensen\n')
print(Steff)



 