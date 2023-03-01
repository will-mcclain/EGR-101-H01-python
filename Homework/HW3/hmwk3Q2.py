## Will McClain
## Question 2

# if user input isn't an int, ask for input again
def input_handler(prompt):
    while True:
        output = input(prompt)
        if not output.isdigit():
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)

def fibonacci(n):
    if n <= 2:
        return 1 # first two starter nums of the fibonacci sequence are 1
    a = 1
    b = 1
    for i in range(2, n): # iterates the sequence n-2 times
        a, b = b, a+b #gotta do it all in one line to swap the values right
    return b

GOLDEN_RATIO = (1 + 5**(1/2)) / 2

def main():
    print("Approximating the Golden Ratio within 10^(-M)")
    M = input_handler("Input an integer...")
    fibonumber = 1 #haha portmanteau
    while abs(fibonacci(fibonumber + 1) / fibonacci(fibonumber) - GOLDEN_RATIO) > 10**(-1*M): # while still out of range
        fibonumber += 1
    print("It takes " + str(fibonumber) + " fibonacci steps to get to the Golden Ratio within 10^(-" + str(M) +")")
    input()

main()

## when M = 9, the step num is 23
