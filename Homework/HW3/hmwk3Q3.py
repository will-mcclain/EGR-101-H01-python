## Will McClain
## Question 3

# if user input isn't an int, ask for input again
def input_handler(prompt):
    while True:
        output = input(prompt)
        if not output.isdigit():
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)

def main():
    print("Finding the GCF of two integers")
    A = input_handler("Enter and integer...")
    B = input_handler("Another one please...")
    big_bro = max(A, B) # never let me name variables
    lil_bro = min(A, B)
    while lil_bro != 0: # go until there is no remainder
        # find remainder of two nums, replaces big num and small num with small num and remainder, repeat
        R = big_bro % lil_bro
        big_bro, lil_bro = lil_bro, R
    print("The GCF of " + str(A) + " and " + str(B) + " is " + str(big_bro))
        

main()

## when A = 98,025,733,547 and B = 2,345,109,894,323, GCF is 7
