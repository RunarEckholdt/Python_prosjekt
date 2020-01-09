# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:51:17 2020

@author: Runar
"""

#import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

#t = sy.symbol('t')
A = 2.5
t = 5

x = np.linspace(0,9,40)

def akselerasjon(A, t):
    a = A * np.exp(-x/t)
    return a

def fart(A,t):
    v = (-1/5)*A*np.exp(-x/t) + 12
    return v

plt.xlabel("t")
plt.ylabel("a")
plt.plot(x,akselerasjon(A,t),"b-")
plt.show()

plt.ylabel("v")
plt.plot(x,fart(A,t), "r-")

print((-1/5)*A*np.exp(-9/t)+12.5)