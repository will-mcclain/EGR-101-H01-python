## Homework 5, Problem 1
## Will McClain
## EGR 101-01
## Due: 2/23/23

import general_functions_2 as gf
import random as r


def rollDieTill6():
    result = 0 #could really be any number that's not 1-6, 0 is arbitrary
    counter = 0
    while result != 6: #until success
        result = r.randint(1,6)
        counter += 1 #keep track of attempts
    return counter

def main():
    roll_list = [rollDieTill6() for i in range(100_000)] #technically a for loop
    print(f"It takes an average of {gf.averageListValues(roll_list)} rolls to get a six")

if __name__ == "__main__":
    main()


#The average output is around 6ish, but check my program for the exact value
#the for loop is in gf.returnAverageHitRate()