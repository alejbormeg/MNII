#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:04:25 2020

@author: Alejandro
"""

import numpy as np 
import sympy as sp
from decimal import getcontext
from decimal import Decimal
import matplotlib.pyplot as plt  
from random import random 

from numpy import sign

def mychop(expr, *, max=10**(-10)):
    if abs(expr) > max:
      return expr 
    else:
      return 0
chop_vec = np.vectorize(mychop)

mporig = getcontext().prec

f = sp.Function('f')
a,h = sp.symbols('a,h')
z = sp.Symbol('z')

x = [a-h,a,a+h]  # nodos que usaremos para la fórmula
y = [f(x[0]),f(x[1]),f(x[2])]  # valores de la función en dichos nodos

p0 = y[0]  # vamos a ir construyendo el polinomio de interpolación usando el método de Newton
p1 = p0 + (z-x[0])/(x[1]-x[0])*(y[1]-y[0])

D = sp.Symbol('D')   # D diferencia dividida a calcular
p2 = p1 + (z-x[0])*(z-x[1])*D # D = f[x0,x1,x2]
p2  # ya tenemos la expresión genérica de dicho polinomio de grado 2 con z como incógnita

print ("Polnomio de interpolación: ")
print (p2)

#Ahora calculamos el valor de D
p2.subs({z:x[0]})==y[0],p2.subs({z:x[1]})==y[1] 

# pero también tenemos aún que garantizar que p(x2) = y2
sol2=sp.solve(p2.subs({z:x[2]})-y[2],D)  # para ello resolvemos la ecuación correspondiente y despejamos el valor de D

D = sol2[0]
print ("\nDonde D vale: ",D)    

p2 = p1 + (z-x[0])*(z-x[1])*D
print("\nPolinomio final de interpolación :", p2)

p2.subs({z:x[2]})==y[2] # que también interpola el valor y[2]

print("\nLa aproximación buscada será el resultado de derivar dos veces el polinomio: ")
print(sp.diff(p2,z,2) )