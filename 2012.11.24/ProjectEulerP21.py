#!/usr/bin/python

'''
This post is dedicated to the memory of Daniel Cox. Daniel was a
fellow Tech student, a great friend, a fantastic programmer, a Mac
fan, a Linux guru, and a brilliant hacker. I was lucky enough to have
known him and to have learned from him during his time here. Daniel, I
will miss you and will always remember the great times we had together
at Tech. Rest in peace friend.
'''

'''
http://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

# import alwaysrememberingfriends
import math
import itertools

# This function determines if Integer is prime by looking for divisors
# up to its square root
def IsPrime(Integer):
    SquareRoot = math.floor(math.sqrt(Integer))

    for i in range(3, SquareRoot+1):
        if Integer % i == 0:
            return False

    return True

# This function generates a list of primes where the last prime in the
# list is the first prime greater than Limit
def GeneratePrimes(Limit):
    PrimesList = [2]
    FoundPrime = False
    Difference = 1
    PossiblyPrime = 0
    Index = 1

    while PossiblyPrime < Limit:
        while FoundPrime == False:
            PossiblyPrime = (2*Index) + Difference

            if IsPrime(PossiblyPrime) == True:
                FoundPrime = True
                PrimesList.append(PossiblyPrime)
                Index += 1
            else:
                Difference += 2

        FoundPrime = False

    return PrimesList

# This function takes all of the number in a tuple and multiplies them
# together, returning the result
def MultiplyNumbers(Tuple):
    Result = 1

    for i in Tuple:
        Result *= i

    return Result

# This function calculates the sum of a number's proper divisors
def SumOfProperDivisors(Number, PrimesList):
    PrimeFactors = []
    PrimeFactorsCombinations = []
    DividingPrimeFactor = True
    FindingPrimeFactors = True
    Sum = 1
    Index = 0
    Temp = Number

    # First get the prime factors of the number
    while FindingPrimeFactors == True:
        DividingPrimeFactor = True

        while DividingPrimeFactor == True:
            if Temp % PrimesList[Index] == 0:
                PrimeFactors.append(PrimesList[Index])
                Temp = Temp // PrimesList[Index]

                if Temp == 1:
                    FindingPrimeFactors = False

            else:
                DividingPrimeFactor = False

        Index += 1

    # If there is ony one prime factor (i.e. the number is prime),
    # then return 1 as 1 is the only proper divisor of a prime number
    if len(PrimeFactors) == 1:
        return 1
    # If there are two or more prime factors, then find the remaining
    # factors of the number from the prime factors. Once all of the
    # remaining factors have been found, sum them and the prime
    # factors and return the sum.
    else:
        for i in range(2, len(PrimeFactors)):
            PrimeFactorsCombinations.extend(list( \
                itertools.combinations(PrimeFactors, i)))

        PrimeFactors = list(set(PrimeFactors))
        PrimeFactorsCombinations = \
            list(set(PrimeFactorsCombinations))

        Divisors = [1]
        for i in PrimeFactors:
            Sum += i
            Divisors.append(i)

        for i in PrimeFactorsCombinations:
            Sum += MultiplyNumbers(i)
            Divisors.append(MultiplyNumbers(i))

        return Sum

def main():
    NumberList = []
    Answer = 0
    Index = 0

    # Find the prime numbers between 1 and 10000 and store them in an
    # array for the prime factorization of numbers.
    PrimesList = GeneratePrimes(10000)

    # Iterate over the numbers between 3 and 9999, finding the
    # sum of each number's proper divisors.
    for i in range(3, 10000):
        NumberList.append(SumOfProperDivisors(i, PrimesList))

    # Find the amicable pairs and sum them
    for i in NumberList:
        if i < len(NumberList):
            if i != (Index + 3) and (Index + 3) == NumberList[i - 3]:
                Answer += (i + Index + 3)
        Index += 1

    # Print the answer
    Answer = Answer // 2
    print(Answer)

if __name__ == "__main__":
    main()
