## Will McClain
## Question 1

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
    # initialize counter for num-to-be-tested and total-num-of-primes
    prime_counter = 0
    test_num = 2
    
    # get user input
    print("Finding the Mth prime number")
    M = input_handler("Enter an integer...")
    
    while prime_counter < M: # while we haven't hit our prime quota
        if determine_prime_TF(test_num): #plug num to be tested into our prime finder
            prime_counter += 1
        test_num += 1 #increment our num to be tested
    test_num -= 1 # the while loop returns our test num + 1 because test_num += 1 runs even after we hit our quota, so we need to compensate for that
    print("Prime #" + str(M) +" is " + str(test_num))
    input()

main()

## when M is 908, output is 7069
