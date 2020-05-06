#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:12:45 2020

@author: Alejandro
"""
import numpy as np
import sympy as sp

x = sp.symbols('x')
z = sp.symbols('z')
a = -1; b = 1;

def f(x):
    return np.exp(x)*x
def fs(x):
    return sp.exp(x)*x

#Definimos la función peso como en teoría
def w(x):
    return abs(x)

print("Fórmula Gaussiana para 2 Nodos")
num_nodos = 2
grado = 2*num_nodos-1
nodos = list(sp.symbols('p0:'+ str(num_nodos)))
coef = list(sp.symbols('c0:'+ str(num_nodos)))
incog = coef + nodos
#Obtenemos las ecuaciones cuyas soluciones serán los nodos de Gauss que usaremos para obtener el máximo grado de exactitud
ecuaciones = [np.dot([(z**i).subs({z:nodos[j]}) for j in range(num_nodos)],coef)-sp.integrate(w(x)*x**i,(x,a,b)) for i in range(grado+1)]
solucionGauss = sp.solve(ecuaciones,incog)

for i in range(num_nodos):
    coef[i] = solucionGauss[0][i]
for i in range(num_nodos):
    nodos[i] = solucionGauss[0][num_nodos+i]

print("Los nodos de la fórmula serán: ", nodos)
print("Los coeficientes de los nodos obtenidos serán: ", coef)
Gaussiana = np.dot([sp.N(fs(nodos[i])) for i in range(num_nodos)],coef)
print("El valor aproximado de la integral es: ",Gaussiana)
valor_exacto = sp.N(sp.integrate(w(x)*fs(x),[x,a,b]))
print("El valor exacto de la integral es: ", valor_exacto )
print("El error cometido es: ", abs(Gaussiana-valor_exacto ))

print("\nGaussiana para 3 nodos")
num_nodos = 3
grado = 2*num_nodos-1
nodos = list(sp.symbols('p0:'+ str(num_nodos)))
coef = list(sp.symbols('c0:'+ str(num_nodos)))
incog = coef + nodos
ecuaciones = [np.dot([(z**i).subs({z:nodos[j]}) for j in range(num_nodos)],coef)-sp.integrate(w(x)*x**i,(x,a,b)) for i in range(grado+1)]
solucionGauss = sp.solve(ecuaciones,incog)

for i in range(num_nodos):
    coef[i] = solucionGauss[0][i]
for i in range(num_nodos):
    nodos[i] = solucionGauss[0][num_nodos+i]
    
print("Los nodos de la fórmula serán: ", nodos)
print("Los coeficientes de los nodos obtenidos serán: ", coef)
Gaussiana = np.dot([sp.N(fs(nodos[i])) for i in range(num_nodos)],coef)
print("El valor aproximado de la integral es: ",Gaussiana)
print("El valor exacto de la integral es: ", valor_exacto )
print("El error cometido es: ", abs(Gaussiana-valor_exacto ))
print("Como podemos observar con la gaussiana de 3 nodos obtenemos un valor mucho más preciso")