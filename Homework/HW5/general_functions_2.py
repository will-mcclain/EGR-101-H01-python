import math as m

def intInputHandler(prompt):
    '''boolean hell'''
    while True:
        output = input(prompt)
        if len(output.rsplit("-")) > 2: #too many dashes
            print("That's not an acceptable value. Try again...")
            continue
        elif len(output.rsplit("-")) == 2:
            if not ((output[0].isdigit() or output[0]== "-") and output.rsplit("-")[1].isdigit()): #make sure both halves of the split string are acceptable
                print("That's not an acceptable value. Try again...")
                continue
        elif len(output.rsplit("-")) == 1:
            if not output.isdigit():
                print("That's not an acceptable value. Try again...")
                continue
        else:
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)

def positiveIntInputHandler(prompt):
    while True:
        output = input(prompt)
        if not output.isdigit() or int(output) < 0 or output == "":
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)

def nonNegativeIntInputHandler(prompt):
    while True:
        output = input(prompt)
        if not output.isdigit() or output == "":
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)


def printList(list_to_print):
    for x in list_to_print:
        print(x)

def averageListValues(input_list):
    return sum(input_list)/len(input_list)


def convertPolarToCartesian(coords):
    x, y = coords["r"] * m.cos(coords["theta"]), coords["r"] * m.sin(coords["theta"])
    return {"x": x, "y": y}

def convertCartesianToPolar(coords):
    r, theta = m.dist([coords["x"], 0], [0, coords["y"]]), m.atan2(coords["y"], coords["x"]) 
    return {"r": r, "theta": theta}


def returnAverageHitRate(boolean_function_list):
    hits = 0
    for boolean in boolean_function_list: #takes a list of function boolean outputs and loops through 'em
        if boolean: #if we see a hit
            hits += 1
    return hits/len(boolean_function_list)