#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:15:21 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp


x = sp.Symbol('x')
def f(x):
    return x**x;

#Calculamos el valor exacto de la segunda derivada para a = 2.5
def d2f(x):
    return (x**x)*((sp.log(x) + 1)**2 + 1/x)

#Calculamos las aproximaciones mediante la fórmula del ejercicio anterior
def d2faprox(a,h):
    return (-2*f(a)+f(a-h)+f(a+h))/h**2

a=2.5
exacto=d2f(a)
print("Valor exacto de la segunda derivada:")
print(exacto)


dersnum = np.array([d2faprox(a,10**-j) for j in range(1,6)])# con h desde 10^0 hasta el valor 10(-5). 
print("\nAproximaciones de la función:")
print(dersnum)  


#Errores cometidos
errores = np.abs(np.array(dersnum) - exacto  )
print("\nErrores cometidos:")
print(errores)                         


