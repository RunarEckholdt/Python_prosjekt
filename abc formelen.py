# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:00:41 2019

@author: Runar
"""
import numpy as np


def factorize(a):
    isFactor = False
    i = 2 
    while not isFactor:
        if(a%i==0):
                isFactor=True
        else:
            i+=1
    return i    
    

def simplify(a,b,c):
    aList = []
    bList = []
    cList = []
    tempA = abs(a)
    tempB = abs(b)
    tempC = abs(c)
    
    
    while tempA>1:
        aList.append(factorize(tempA))  #finner neste faktor for tallet og legger den til i listen
        tempA= tempA/aList[-1]          #"fjerner" faktoren fra tallet ved å dividere den ut -1 for siste verdi i listen
    while tempB>1:
        bList.append(factorize(tempB))
        tempB = tempB/bList[-1]
    while tempC>1:
        cList.append(factorize(tempC))
        tempC = tempC/cList[-1]
    
    for x in range(len(aList)):
        if((aList[x]in bList or b==0) and (aList[x]in cList or c == 0)): #hvis verdien i aList for index x er faktor i både bList og cList
            print("Factorized out",aList[x])
            a = a/aList[x]
            b = b/aList[x]
            c = c/aList[x]
            try:
                bList.pop(bList.index(aList[x])) #fjerner faktorene ettersom de er "dividert" bort
            except:
                print("No index for the factor in b")
            try:
                cList.pop(cList.index(aList[x])) 
            except:
                print("No index for the factor in c")
     
    return [a,b,c]

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
    print("Solving expression " + str(a) +"x^2 " + str(b) + "x "+ str(c) + " = 0")
    simplified = simplify(a,b,c)
    a = int(simplified[0])
    b = int(simplified[1])
    c = int(simplified[2])
    print(c)
    
    print("Expression Simplified to: "+ str(a) + "x^2 " + str(b) + "x " + str(c) + " = 0")
    
    x1 = abc_formel1(a,b,c)
    x2 = abc_formel2(a,b,c)
    
    if(x1!="No solution to the problem" and x2!="No solution to the problem"):
        print("X =", x1, "og X =", x2)
    else:
        print(x1)
    main()
        
    


main()
