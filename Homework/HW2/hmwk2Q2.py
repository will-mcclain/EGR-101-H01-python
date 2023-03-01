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

factors = []

def main():
    N = input_handler("Enter an integer...")
    for i in range(1, N):
        # if N is divisible by i, then it's a factor
        if N % i == 0:
            factors.append(i)
    print(factors)
    input()

main()
