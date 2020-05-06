#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:24:10 2020

@author: Alejandro
"""
import sympy as sp

x = sp.symbols('x')

def f(x):
    return x**x;

a = 1;
b = 2;
n = 100; #Numero de partes en que dividiremos el intervalo [1,2]
h = (b-a)/n #Amplitud de cada subintervalo

print("Aplicamos la fórmula del rectángulo derecha compuesta")
rectangulo_derecha = 0;
for i in range(0,100):
    rectangulo_derecha = rectangulo_derecha + f(a+(i+1)*h)
rectangulo_derecha = rectangulo_derecha*h
print(rectangulo_derecha)

print("Aplicamos la fórmula del rectángulo izquierda compuesta")
rectangulo_izda = 0;
for i in range(0,100):
    rectangulo_izda = rectangulo_izda + f(a+i*h)
rectangulo_izda = rectangulo_izda*h
print(rectangulo_izda)

print("Aplicamos la fórmula de Simpson compuesta")
f1 = 0; f2=0
for i in range (1,n+1):
    f1+=f(a+(i-1/2)*h)
for i in range (1,n):
    f2 = f2+f(a+i*h)
total = f(a)+f(b)+4*f1+2*f2
resultado = total *h /6
print(resultado)

print("Aplicamos la fórmula del trapecio compuesta")
f3 = 0
for i in range(1,n):
    f3 = f3+f(a+i*h)
total = f(a)+f(b) +2*f3
resultado = total *h /2
print(resultado)
    
