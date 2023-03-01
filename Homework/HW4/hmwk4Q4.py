## Homework 4, Problem 4
## Will McClain
## EGR 101-01
## Due: 2/16/23

import random as r
import general_functions


def myBirthday(N):
    '''For a room of N people, returns True if anyone's birthdate matches an individual's'''
    #day 1 is Jan 1, day 365 is Dec 31
    my_birthday = r.randint(1,365)
    birthdates = [r.randint(1,365) for i in range(N)] #quick list of N dates
    if my_birthday in birthdates: #if there's a match
        return True
    return False

def main():
    num_people = general_functions.positiveIntInputHandler("Throw me an integer...")
    birthday_boolean = myBirthday(num_people) #True if match, False if no match

    #grammar lmao
    if num_people == 1:
        print("In a room of one person...")
    else:
        print("In a room of " + str(num_people) + " people...")

    #output result
    if birthday_boolean:
        print("Someone shares your birthday!")
    else:
        print("No one has your birthday...")
    input()


if __name__ == "__main__":
    main()
