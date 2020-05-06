#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:45:54 2020

@author: Alejandro
"""
import numpy as np
import sympy as sp


x = sp.symbols('x')
f = sp.Function('f')
a = 0; b = 9;
#DNI 26504975M
def p(x):
    return 2+6*x+5*x**2+0*x**3+4*x**4+9*x**5+7*x**6+5*x**7


sp.plot(p(x),(x,a,b))
print ("Como podemos ver en el gráfico, la función se presta a cometer grandes errores de aproximación usando fórmulas simples o compuestas con nodos equiespaciados, por eso usaremos métodos que se adaptan mejor a este tipo de funciones")
print("\n\nRomberg")
#Necesitamos la fórmula del trapecio compuesto
def trapecio_compuesto(f,n):
    h = (b-a)/n
    f3 = 0
    for i in range(1,n):
        f3 = f3+f(a+i*h)
    total = f(a)+f(b) +2*f3
    resultado = total *h /2
    return resultado

N = 7 #Profundidad máxima de la primera columna
matriz = []
for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append(0)
        
for i in range (N):
    matriz[i][0] = trapecio_compuesto(p,2**i)

print("Matriz de Romberg: ")
print(matriz)

for j in range (1,N):
    for i in range (j,N):
        matriz[i][j] = (4**j*matriz[i][j-1] - matriz[i-1][j-1])/(4**j-1)
        
    
print("Valor aproximado usando Romberg ", matriz[N-1][N-1])
print("Valor exacto de la integral: ",sp.N(sp.integrate(p(x),[x,a,b])))
print ("\n Ahora usaremos el método de integración adaptativa")
tol = 7
epsilon  = 10**(-tol)

def S(a,b):
    h = (b-a)/2
    m = (a+b)/2
    return h/3*(p(a)+4*p(m)+p(b))

total = 0

def diferencia(a,b, epsilon):
    m = (a+b)/2
    if (abs(S(a,b)-S(a,m)-S(m,b)) > epsilon):
        diferencia (a, m,  epsilon/2)
        diferencia (m, b, epsilon/2)
    else:
        global total
        total+=S(a,b)
        


diferencia(a,b,epsilon)

print ("Valor aproximado: ",total)
print("Valor exacto de la integral: ",sp.N(sp.integrate(p(x),[x,a,b])))

