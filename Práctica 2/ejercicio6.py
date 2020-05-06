#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:01:40 2020

@author: Alejandro
"""
import numpy as np
import sympy as sp

x = sp.symbols('x')
def f(x):
    return np.exp(x)*x**15
def fs(x):
    return sp.exp(x)*x**15

#Intervalo de definición [0,2]
a = 0
b = 2

n = 10
h = (b-a)/n #Amplitud de los subintervalos de partida
tol = 10**(-2)
dif = 100
f1 = 0; f2=0

for i in range (1,n+1):
    f1+=f(a+(i-1/2)*h)
for i in range (1,n):
    f2 = f2+f(a+i*h)

x1 = (f(a)+f(b)+4*f1+2*f2)*h/6

x2 = 0   

#Vamos aumentando el numero de subintervalos de la forma 10 20 40 80 ... y paramos cuando la diferencia sea menor que la tolerancia
while (dif > tol):
    n = n*2 #Nuevo número de subintervalos
    h = (b-a)/n #nueva amplitud de los subintervalos
    f1 = 0; f2=0
    for i in range (1,n+1):
        f1+=f(a+(i-1/2)*h)
    for i in range (1,n):
        f2+=f(a+i*h)
    x2 = (f(a)+f(b)+4*f1+2*f2)*h/6
    dif = abs(x2-x1)    
    x1 = x2

print("La aproximación buscada es: ", x2)

print("\nEl valor exacto de la integral es: ",sp.N(sp.integrate(fs(x),[x,a,b])))
print("\nEl error cometido es: ", abs(sp.N(sp.integrate(fs(x),[x,a,b]))-x2))