## Homework 5, Problem 5
## Will McClain
## EGR 101-01
## Due: 2/23/23

import general_functions_2 as gf
import random as r
import math as m


def compareChordLength_TF():
    points = [{"r": 1, "theta": r.uniform(0, 2 * m.pi)} for i in range(2)] #generate random points on circle
    points = [gf.convertPolarToCartesian(x) for x in points] #cartesianize them
    if m.dist([points[0]["x"], points[0]["y"]], [points[1]["x"], points[1]["y"]]) > 1: #check if longer than radius
        return True
    return False

def main():
    N = 10000
    print(f"There's a {round(gf.returnAverageHitRate([compareChordLength_TF() for i in range(N)])*100, 2)}% chance a unit circle's chord is longer than its radius")

if __name__ == "__main__":
    main()


#the for loop is in gf.returnAverageHitRate()