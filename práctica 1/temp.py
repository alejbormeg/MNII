# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def buscaraiz(f,a,b,dx): 
    x1 = a; x2 = a + dx
    f1 = f(x1); f2 = f(x2)
    while sign(f1) == sign(f2):
        if x1 >= b: return None,None
        x1 = x2;  f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2