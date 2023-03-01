## Homework 5, Problem 4
## Will McClain
## EGR 101-01
## Due: 2/23/23


import general_functions_2 as gf
import random as r


def returnLengths(breaks_list, full_length=1):
    '''takes a list of break points and returns a list of broken lengths'''
    lengths = []
    breaks_list.sort() #needs to be in ascending order to avoid negative lengths
    for i in range(len(breaks_list)):
        lengths.append(breaks_list[i]) #the ith length is equal to the leftmost break
        breaks_list = [x - lengths[i] for x in breaks_list] #shift all the break points left bc the i-1th break doesn't count anymore
        full_length -= lengths[i] #keep track of the full length of the stick
    lengths.append(full_length) #append the final length
    return lengths
    


def main():
    N = 10_000

    meta_length_lists = { #intialize dictionary
        "small": [],
        "medium": [],
        "large": []
    }
    
    for i in range(N):
        breaks_list = [r.random() for i in range(2)] #randomized list of break points
        lengths = returnLengths(breaks_list[:]) #gives back as list of lengths
        if not lengths == sorted(lengths):
            lengths.sort()
        meta_length_lists["small"].append(lengths[0]) #fill out our meta_length_lists dictionary
        meta_length_lists["medium"].append(lengths[1])
        meta_length_lists["large"].append(lengths[2])
        
    avg_smallest = gf.averageListValues(meta_length_lists["small"]) #list averaging method from general_functions.py
    avg_mediumest = gf.averageListValues(meta_length_lists["medium"])
    avg_largest = gf.averageListValues(meta_length_lists["large"])

    print(f"The averge smallest length is {round(avg_smallest, 3)}")
    print(f"The avergae medium length is {round(avg_mediumest, 3)}")
    print(f"The average longest length is {round(avg_largest, 3)}")


if __name__ == "__main__":
    main()