## Homework 4, Problem 5
## Will McClain
## EGR 101-01
## Due: 2/16/23

import random as r
from hmwk4Q4 import *
import general_functions


def loopThroughTrials(i, trial_num):
    '''takes the average pass ratio of N trials'''
    match_count = 0
    for j in range(trial_num):
        if myBirthday(i): #imported from hmwk4Q4
            match_count += 1 #if there's a match, increment count
    return match_count/trial_num #likelihood of successes is matches/total trials

def loopThroughPeople(trial_num):
    '''makes a list of average success percentages with the number of people varying from 2 to 400'''
    percentage_list = []
    for i in range(2, 401):
        percentage_string = str(round(loopThroughTrials(i, trial_num)*100, 3))+"%"
        percentage_list.append(percentage_string) # find average of n trials for each num of people 2-400, add to list
    return percentage_list

def main():
    #self-explanatory

    print("Probability of passing for 2-400 people (100 trials):")
    print("\nLoading content...\n")
    general_functions.printList(loopThroughPeople(100))
    
    print("\n\nProbability of passing for 2-400 people (1000 trials):")
    print("\nLoading content...\n")
    general_functions.printList(loopThroughPeople(1000))

    print("\n\nProbability of passing for 2-400 people (10000 trials):")
    print("\nLoading content...\n")
    general_functions.printList(loopThroughPeople(10000))

    input()


if __name__ == "__main__":
    main()

## I generate lists but I present them as N lines of strings
## The list is in the output of loopThroughPeople() before it gets passed through printList()
