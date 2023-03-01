## Homework 4, Problem 2
## Will McClain
## EGR 101-01
## Due: 2/16/23

import math as m
import general_functions

def abr_pi(N):
    '''approximates pi'''
    total = 0
    for n in range(N): #for n terms
        total += (2 * (-1)**n * 3**(1/2 - n))/(2*n + 1) #add the next term to the total
    return total

def main():
    N = general_functions.positiveIntInputHandler("Throw me a positive integer...") #get N from user
    print("There's a " + str(abs(abr_pi(N)-m.pi)) + " difference bewtween the Abraham Series approximation and pi when N is " + str(N))
    input()

if __name__ == "__main__":
    main()
