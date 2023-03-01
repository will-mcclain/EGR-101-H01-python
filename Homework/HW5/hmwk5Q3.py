## Homework 5, Problem 3
## Will McClain
## EGR 101-01
## Due: 2/23/23

import general_functions_2 as gf
import random as r


def tossCoin():
    coin_coords = { #give random landing coords
        "x": r.random(),
        "y": r.random()
    }
    if coin_coords["x"] >= 3/8 and coin_coords["x"] <= 1 - 3/8 and coin_coords["y"] >= 3/8 and coin_coords["y"] <= 1 - 3/8: #if it fits on the table
        return True
    return False

def main():
    N = 10_000

    print(f"You have a {round(gf.returnAverageHitRate([tossCoin() for i in range(N)])*100, 2)}% chance of landing the coin entirely within the bounds of the table")


if __name__ == "__main__":
    main()


#the for loop is in gf.returnAverageHitRate()