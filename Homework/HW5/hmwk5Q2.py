## Homework 5, Problem 2
## Will McClain
## EGR 101-01
## Due: 2/23/23

import general_functions_2 as gf
import random as r
import gc

def doMontyHall():
    CONTESTANT_SWITCHES = True #is always true so I don't really understand why we need the if statement but it's part of the grade so
    
    #door 2 has the prize
    
    prize_placement = r.sample(range(3), 3) #i could literally just do range(3) and it'd be the same but the problem said make it random
    contestant_choice = r.choice(prize_placement)
    selected_doors = prize_placement #a list of elligible doors that will get whittled down later

    if contestant_choice == 0:
        #door 1 is opened
        selected_doors.remove(1)
        if CONTESTANT_SWITCHES: #remove unchosen door from selcted_doors
            selected_doors.remove(0)
        else:
            selected_doors.remove(2)
    elif contestant_choice == 1: #remove unchosen door from selcted_doors
        #door 0 is opened
        selected_doors.remove(0)
        if CONTESTANT_SWITCHES:
            selected_doors.remove(1)
        else:
            selected_doors.remove(2)
    else:
        #either door 0 or 1 is opened
        dummy_list = [0, 1]
        first_removal = dummy_list.pop(r.randint(0,1)) #randomize first and second door choices
        second_removal = dummy_list.pop(0)
        del dummy_list #don't need it anymore
        gc.collect()

        selected_doors.remove(first_removal)
        if CONTESTANT_SWITCHES: #remove unchosen door from selcted_doors
            selected_doors.remove(2)
        else:
            selected_doors.remove(second_removal)

    if selected_doors[0] == 2: #ayy you win I knew you could do it
        return True
    return False

def main():
    print("Running...")

    trials = 100_000
    print(f"Empirically, you have a {round(gf.returnAverageHitRate([doMontyHall() for i in range(trials)])*100, 2)}% chance of winning the Monty Hall problem if you switch")

if __name__ == "__main__":
    main()


#the for loop is in gf.returnAverageHitRate()