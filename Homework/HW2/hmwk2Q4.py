## Will McClain
## Question 4

# if user input isn't an int, ask for input again
def input_handler(prompt):
    while True:
        output = input(prompt)
        if not output.isdigit():
            print("That's not an acceptable value. Try again...")
            continue
        break
    return int(output)

def determine_prime_TF(N):
    factors = []
    for i in range(1, N):
        # if N is divisible by i, then it's a factor
        if N % i == 0:
            factors.append(i)
    # if size of factors list is exactly one, its prime, if more or 0, it's composite
    if len(factors) == 1:
        return True
    return False




def main():
    # take int form user
    M = input_handler("Enter an integer...")
    # set counter to 0
    # I have to declare it inside the main() function and idk why but oh well
    primes_count = 0
    # big loop
    for N in range(1, M+1):
        # lil loop contained in determine_prime_TF()
        if determine_prime_TF(N):
            # increment counter
            primes_count += 1
    print(primes_count)
    input()

main()
