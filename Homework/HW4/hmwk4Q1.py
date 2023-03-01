## Homework 4, Problem 1
## Will McClain
## EGR 101-01
## Due: 2/16/23

import general_functions

def isPrime(N):
    factors = []
    for i in range(1, N):
        # if N is divisible by i, then it's a factor
        if N % i == 0:
            factors.append(i)
    # if size of factors list is exactly one, its prime, if more or 0, it's composite
    if len(factors) == 1:
        return True
    return False

def tallyPrimes(M):
    primes_count = 0
    for N in range(1, M+1):
        if isPrime(N): #if you stumble upon a prime, tick up the counter
            primes_count += 1
    return primes_count

def main():
    while True: 
        M = general_functions.positiveIntInputHandler("Give me an integer greater than 1...")
        if M < 2: #gotta be >1 and I don't wanna write a new general_function
            print("Your value is too small...")
            continue
        break

    print("There are " + str(tallyPrimes(M)) + " prime(s) between 2 and " + str(M) + " inclusive")
    input()
    
main()
