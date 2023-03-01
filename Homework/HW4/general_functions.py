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
