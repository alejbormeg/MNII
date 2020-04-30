# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:19:00 2020

@author: Alejandro
"""

import numpy as np
import sympy as sp
from decimal import getcontext
from decimal import Decimal

from numpy import sign

from scipy.optimize import fsolve
from sympy.solvers import solve, nsolve, solveset


print("a) f(x)=x^7-x^4+2")
coefs = [1,0,0,-1,0,0,0,2]

print(np.roots(coefs));


x = sp.Symbol('x')

print("b) f(x) = x^7 +cosx -3")

print(nsolve(x**7+sp.cos(x)-3,x,1))