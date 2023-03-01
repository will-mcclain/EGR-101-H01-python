## Will McClain
## Question 5


def numInputHandler(prompt):
    while True:
        output = input(prompt)
        if not output.replace('.', '', 1).isdigit(): # accepts ints and floats now
            print("That's not an acceptable value. Try again...")
            continue
        break
    if "." in output:
        return float(output)
    return int(output)

def questionHandler(question):
    while True: #run until user gives something that makes some sense like geez
        response = input(question)
        if response.lower() == "y" or response.lower() == "n" or response.lower() == "yes" or response.lower() == "no":
            break
        print("This is a yes or no answer...")
    return response.lower()

def populateList():
    populated_list = []
    print("Let's populate an empty list")
    while True: #repeat until user says yes
        populated_list.append(numInputHandler("Throw me a number..."))
        done = questionHandler("You done? [y/n]")
        if done == "y" or done == "yes":
            break
    return populated_list #return dirty, unsorted list

def swap(sample_list, a, b):
    sample_list[a], sample_list[b] = sample_list[b], sample_list[a]
    return sample_list
    

def main():
    unsorted_list = populateList()
    unsorted_list_copy = unsorted_list #we're gonna need this copy later
    sorted_list = []
    while len(unsorted_list) > 0: #while there's still work to do
        unsorted_list = swap(unsorted_list[:], 0, unsorted_list.index(min(unsorted_list))) #swap first element with smallest element
        sorted_list.append(unsorted_list.pop(0)) #take smallest element and push it to sorted_list
    print("The list you gave looks like " + str(unsorted_list_copy))
    print("Sorted out it looks like " + str(sorted_list))
    input()

main()
