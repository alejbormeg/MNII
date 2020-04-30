# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:03:34 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp
from decimal import getcontext


def mychop(expr, *, max=10**(-10)):
    ''' Esta función redondea por cero cualquier número más
    pequeño a la cantidad máxima indicada'''
    if abs(expr) > max:
      return expr 
    else:
      return 0
chop_vec = np.vectorize(mychop)
mporig=getcontext().prec


def horner(a,x):#implementa metodo de horner
        if len(a)==1: #En la lista estan los coeficientes del polinomio
            return a[0] #Y en X el valor a evaluar
        else:
            return a[0] + x * horner(a[1:],x)

print ('Ejemplo para calcular el desarrollo de taylor del polinomio x^3+2x^2-x+9')
x=sp.Symbol('x')
def f(x):
    return x**3+2*x**2-x+9

def derivada_iesima(f,n,m):
    for i in range(n):
        f=f.diff(x)
    values = {x: m}
    return f.evalf(subs=values)

def factorial (n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)

def taylor(f,a,n): #Derrollo de taylor de f centrado en a hasta el término n
   for i in range (n):
       taylor=1/factorial(i)*derivada_iesima(f,i,a)*(x-a)**i
       if(i!=0):
           if (derivada_iesima(f,i,a)>0):
               print ("+",taylor,end="")
           else: 
               print (taylor,end="")
       else:
           print(taylor,end="")
print()
       
        
print("Desarrollo de taylor=" )
a= int(input ("\n Ingrese en que punto quiere centrado el polinomio >>"))
n= int(input ("\n Ingrese hasta que termino quiere hacer el desarrollo de taylor >>"))
taylor(f(x),a,n)
    

print("\n\nMetodo N-R usando Horner para evaluar el polinomio\n")
def p (x):
    return 2+6*x+5*x**2+4*x**4+9*x**5+7*x**6+5*x**7

def dp(x):
    return 6+10*x+16*x**3+45*x**4+42*x**5+35*x**6

coef=[2,6,5,0,4,9,7,5]
coef_der=[6,10,0,16,45,42,35]

def gNR(x, coef,coef_der):
    '''función de punto fijo asociada al método de N-R para f(x)'''
    return x - horner(coef,x)/horner(coef_der,x)
    
print ('Solución con N-R clásico')
a=-1.; b=1.; 
x0 = sp.N(a); aproxNR = [x0]; niter = 10;
for k in range(niter):
    x1 = gNR(x0,coef,coef_der); x0 = x1
    aproxNR.append(x1)
print(aproxNR)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    