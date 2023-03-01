# Will McClain
# Python Project
# EGR 101-H01
# Due Date: 2/28/2023


import math as m
import random as r
from matplotlib import pyplot as plt


def returnAverageHitRate(boolean_list):
    hits = 0
    for boolean in boolean_list:#takes a list of boolean outputs and loops through 'em
        if boolean:#if we see a hit
            hits += 1
    return hits/len(boolean_list)

def convertCylindricalToCartesian(coords):
    x, y, z = coords["r"] * m.cos(coords["theta"]), coords["r"] * m.sin(coords["theta"]), coords["z"]#standard conversion formulas
    return {"x": x, "y": y, "z": z}

def placePlanetReturnCoords():
    cylindrical_planet_coords = {#randomize coords for a single planet in cylindrical
        "r": r.uniform(15_000, 50_000),
        "theta": r.uniform(0, 2 * m.pi),
        "z": r.uniform(-500, 500)
    }
    
    return convertCylindricalToCartesian(cylindrical_planet_coords)#and convert to cartesian to use later

def checkPlanetInRange_TF(cartesian_planet_coords):
    RADIO_RANGE = 15 #a constant
    CYLINDRICAL_EARTH_COORDS = {"r": 25_800, "theta": m.pi, "z": 0}#a constant
    CARTESIAN_EARTH_COORDS = convertCylindricalToCartesian(CYLINDRICAL_EARTH_COORDS)#a constant
    return (cartesian_planet_coords["x"] - CARTESIAN_EARTH_COORDS["x"])**2 + (cartesian_planet_coords["y"] - CARTESIAN_EARTH_COORDS["y"])**2 + (cartesian_planet_coords["z"] - CARTESIAN_EARTH_COORDS["z"])**2 <= RADIO_RANGE**2#a boolean, true if planet in range

def checkMultiplePlanetsInRange_TF(N):
    for i in range(N):#do checkPlanetInRange_TF for however many random planets there are
        planet_coords = placePlanetReturnCoords()#pick a random planet spot
        if checkPlanetInRange_TF(planet_coords):
            return True#break immediately if we have a hit
    return False

def main():
    print("Running...")
    
    TRIAL_NUM = 10#can be increased but my laptop is tired, boss
    probabilities_list = []
    for planet_num in range(100_000_000, 1_100_000_000, 100_000_000):#for each increment in num of planets
        made_contact_boolean_list = [checkMultiplePlanetsInRange_TF(planet_num) for i in range(TRIAL_NUM)]#a list of booleans containing the outputs of our galaxy-wide searches TRIAL_NUM times
        contact_rate = returnAverageHitRate(made_contact_boolean_list)#get our average success rate from general_functions
        probabilities_list.append(contact_rate)#tack that onto our probabilities list


    print(probabilities_list)#which is now looks smth like [0.2, 0.3, 0.2, 0.6, 0.5, 0.7, 0.7, 0.9, 1.0, 0.9], generally increasing with element num
    
    plt.plot(list(range(100, 1_100, 100)), probabilities_list)#plot it
    plt.xlabel("Lifeforms (millions)")#give it labels
    plt.ylabel("Probability of contact (0-1)")
    plt.title(f"Likelihood of Detecting Lifeforms in the Milky Way Galaxy with Respect to Number of Lifeforms ({TRIAL_NUM} Trials)")#and a title
    plt.show()#and finally show it

    print("Done!")#tada


if __name__ == "__main__":
    main()