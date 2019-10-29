# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:00:41 2019

@author: Runar
"""
import numpy as np


def abc_formel1(a, b, c):
    #(-b+sqrt(b^2-4*a*c))2*a
    try:
        if(b**2-4*a*c>=0):
            x1= (-b+np.sqrt((b**2)-4*a*c))/2*a
        else:
                x1 = ("No solution to the problem")
        return x1

    except:
        print("Error...")
        main()
    
    
def abc_formel2(a, b, c):
    #(-b-sqrt(b^2-4*a*c))2*a
    try:
        if(b**2-4*a*c>=0):
            x2= (-b-(np.sqrt((b**2)-4*a*c)))/2*a
        
        else:
            x2 = ("No solution to the problem")
        
    
        return x2
    except:
        print("Error...")
        main()

def main():
    a = input("Type in a: ")
    b = input("Type in b: ")
    c = input("Type in c: ")

    try:
        a=int(a)
        b=int(b)
        c=int(c)
    except:
        print("That is not a valid input")
        main()
        

    x1 = abc_formel1(a,b,c)
    x2 = abc_formel2(a,b,c)
    
    if(x1!="No solution to the problem" and x2!="No solution to the problem"):
        print("X =", x1, "og X =", x2)
    else:
        print(x1)
    main()
        
    


main()
