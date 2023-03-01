## Homework 4, Problem 3
## Will McClain
## EGR 101-01
## Due: 2/16/23

from hmwk4Q2 import abr_pi
import math as m
import general_functions


def main():
    terms_needed = 1
    M = general_functions.intInputHandler("Throw me an integer...") #get M value first
    while abs(abr_pi(terms_needed)-m.pi) > 10**(-M): #for as long as we're not "close enough"
        terms_needed += 1 #self-explanatory
    print("To be within 10^(-" + str(M) + ") of pi, " + str(terms_needed) + " term(s) are needed")
    input()
        

if __name__ == "__main__":
    main()


##when M=9, output is 17
