## Will McClain
## Question 4

##I've decided to use camel case for functions from now on don't ask me why

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

def swap(sample_list, a, b): #self-explanatory
    sample_list[a], sample_list[b] = sample_list[b], sample_list[a]
    return sample_list

def bubbleUp(unbubbled_list):
    for i in range(len(unbubbled_list)-1): #you can't bubble the last element because there's nothing to bubble it with
        if unbubbled_list[i+1] < unbubbled_list[i]: #if in need of bubbling
            unbubbled_list = swap(unbubbled_list, i, i+1) #then bubble
    return unbubbled_list

def main():
    unsorted_list = populateList()
    sorted_list = unsorted_list #but not for long >:)
    while sorted_list != sorted(unsorted_list): # for as long as the list isn't sorted
        sorted_list = bubbleUp(sorted_list[:]) #have to pass in a copy or else it sorts a list it shouldn't
    print("The list you gave looks like " + str(unsorted_list))
    print("Sorted out it looks like " + str(sorted_list))
    input()

main()
