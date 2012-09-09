#!/usr/bin/python

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import sys
import math

# Returns the prime factors of an odd integer in a list
def GetPrimeFactors(Integer):

    Limit = math.floor(math.sqrt(Integer))
    Divisor = 3
    IntegerIsPrime = True
    PrimeFactors = []

    # While we are not yet at the square root of Integer, look for
    # integers that divide into it
    while Divisor <= Limit:
        if Integer % Divisor == 0:
            # If Integer is divisible by two numbers, get their prime
            # factors and add them to the list of prime factors
            PrimeFactors.extend(GetPrimeFactors(Divisor))
            PrimeFactors.extend(GetPrimeFactors(Integer // Divisor))
            IntegerIsPrime = False
            break

        Divisor = Divisor + 2

    # If Integer is prime, append it to the list so that it
    # can be returned
    if IntegerIsPrime == True:
        PrimeFactors.append(Integer)

    return PrimeFactors

def main():

    Number = 600851475143
    PrimeFactors = []

    # Get the prime factors of the number
    PrimeFactors = GetPrimeFactors(Number)

    # The largest prime factor is the last one that was added
    # to the list
    LargestPrimeFactor = PrimeFactors[len(PrimeFactors) - 1]

    # Print the answer
    print(LargestPrimeFactor)

    sys.exit(0)

if __name__ == "__main__":
    main()
