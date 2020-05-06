#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:35:26 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp

x = sp.Symbol('x')

def f(x):
    return (x**2 + 40)/(x+7+(5*x)**(1/2))


""" 
    Primera aproximación
"""
def derivadaaprox(a,h):
    return (f(a+h)-f(a))/h

derivada = sp.diff(f(x),x)

valor_real = []
aprox = []
errores = []

for i in range(1,10):
    
     valor_exact = derivada.subs({x:i})
     valor_real.append( valor_exact)
     
     aprox.append(derivadaaprox(i, 10**-3))
     
     errores.append(np.abs(valor_exact - aprox[i-1]))
     
print('Fórmula que utilizaremos:')
print('(f(a+h)-f(a))/h')

print('\nValor exacto de las derivadas')
print(valor_real)

print('\nAproximaciones i=1..10')
print(aprox)

print('\nErrores cometidos:')
print( errores)


"""
    Segunda Aproximación
"""

print('\n\nRepetiremos el ejercicio usando la Fórmula Centrada:')

def derivadaaprox(a,h):
    return (f(a+h)-f(a-h))/2*h

valor_real = []
aprox = []
errores = []

for i in range(1,10):
     valor_exact = derivada.subs({x:i})
     valor_real.append( valor_exact)
     
     aprox.append(derivadaaprox(i, 10**-3))
     
     errores.append(np.abs(valor_exact - aprox[i-1]))
     

print('(f(a+h)-f(a-h))/2h')

print('\nValor exacto de las derivadas')
print(valor_real)

print('\nAproximaciones i=1..10')
print(aprox)

print('\nErrores cometidos:')
print( errores)

"""
    Tercera aproximación
"""

print('\n\n Finalmente repetiremos el ejercicio con la fórmula del Ejercicio 1:')

def d2faprox(a,h):
    return (-2*f(a)+f(a-h)+f(a+h))/h**2

d2f = sp.diff(f(x),x,2)

valor_real = []
aprox = []
errores = []

for i in range(1,10):
     valor_exact = d2f.subs({x:i})
     valor_real.append( valor_exact)
     
     aprox.append(d2faprox(i, 10**-3))
     
     errores.append(np.abs(valor_exact - aprox[i-1]))
     

print('(-2*f(a)+f(a-h)+f(a+h))/h**2')

print('\nValor exacto de las derivadas')
print(valor_real)


print('\nAproximaciones i=1..10')
print(aprox)

print('\nErrores cometidos:')
print( errores)
