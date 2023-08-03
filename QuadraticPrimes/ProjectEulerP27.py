#!/usr/bin/python3

'''
http://projecteuler.net/problem=27

Euler published the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the
consecutive values n = 0 to 39. However, when n = 40,
40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 − 79n + 1601 was
discovered, which produces 80 primes for the consecutive values
n = 0 to 79. The product of the coefficients, −79 and 1601,
is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
'''

import math

# This function determines if Integer is prime by looking for divisors
# up to its square root
def IsPrime(Integer):
    if Integer % 2 == 0:
        return False

    SquareRoot = math.ceil(math.sqrt(abs(Integer)))
 
    for i in range(3, SquareRoot):
        if Integer % i == 0:
            return False
 
    return True

# This function generates a list of all primes less than Limit
def GeneratePrimes(Limit):
    PrimesList = [2]
    FoundPrime = False
    Offset = 1
    PossiblyPrime = 0
    Index = 1
 
    while PossiblyPrime < Limit:
        while FoundPrime == False:
            PossiblyPrime = (2*Index) + Offset
 
            if IsPrime(PossiblyPrime) == True:
                FoundPrime = True
                PrimesList.append(PossiblyPrime)
                Index += 1
            else:
                Offset += 2
        
        FoundPrime = False
 
    return PrimesList[0:len(PrimesList) - 1]

def GetQuadraticSequenceLength(b, a):
    IsPrimeValue = True
    SequenceLength = 0
    n = 0

    while IsPrimeValue == True:
        if(IsPrime((n**2) + (a*n) + b) == True):
            SequenceLength += 1
            n += 1
        else:
            IsPrimeValue = False

    return SequenceLength

def main():
    SequenceLength = 0
    LongestSequenceLength = 0
    LongestSequenceLengthProduct = 0

    # b can only be a prime number because the series must start with
    # n = 0
    PositiveBList = GeneratePrimes(1000)
    BList = [x*-1 for x in PositiveBList]
    BList.reverse()
    BList.extend(PositiveBList)

    AList = list(range(-999, 1))
    AList.extend(list(range(1, 1000)))

    for b in BList:
        for a in AList:
            SequenceLength = GetQuadraticSequenceLength(b, a)

            if(SequenceLength > LongestSequenceLength):
                LongestSequenceLength = SequenceLength
                LongestSequenceLengthProduct = a*b

    print(LongestSequenceLengthProduct)

if __name__ == "__main__":
    main()
