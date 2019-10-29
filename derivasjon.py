
"""
Created on Wed Oct 23 09:10:12 2019

@author: Runar
"""

#kan bare derivere simple polynom utrykk, ikke kjerne regel, sin, cos, kvotient eller produkt


#  (f(x+h)-f(x))/(h)
# der h = deltaX

import sympy  as sy

#x, h = sy.symbols("x h")
x = sy.Symbol('x')
h = sy.Symbol('h')

   
def main():
    print("Don't forget * for multiplication ^.^")
    f = input("F(x)= ")
    f=f.lower()
    derF = derivate(f)
    
    
    
    print(derF, "\n\n\n")
    main()

def derivate(f):
    
    
    
    try:
        #definerer f(x + deltaX)
        fh=f.replace("x","(x+h)")
    
        #gjør f og fh fra String til utrykk
        fh = sy.sympify(fh)
        f = sy.sympify(f)
        
        #definisjonen av den deriverte
        der = (fh-f)/h
        
        #utfører mulig multiplikasjoner og divisjoner
        der = sy.expand(der)
        
        #setter deltaX til 0
        der = der.subs({h:0})
        
    except:
        print("Error...")
        main()
       
    return der



main()