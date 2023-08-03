#!/usr/bin/python

'''
http://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.
'''

import math

# Find all the proper divisors of a number and return them as a set
def GetProperDivisors(Integer):
    ProperDivisors = set([1])

    for i in range(2, math.floor(math.sqrt(Integer)) + 1):
        if Integer % i == 0:
            ProperDivisors.add(i)
            ProperDivisors.add(Integer // i)

    return ProperDivisors

# Determine if a number is abundant by calculating its proper divisors
# and getting their sum
def IsAbundant(Integer):
    if sum(GetProperDivisors(Integer)) > Integer:
        return True
    else:
        return False

def main():
    Limit = 28124
    Answer = 0
    NumberList = set(range(1, Limit))
    AbundantNumbers = set()

    # Find all of the abundant numbers from 12 to 28123
    for i in range(12, Limit):
        if IsAbundant(i) == True:
            AbundantNumbers.add(i)

    # Check each number from 1 to 28123 to determine if each one can
    # be written as the sum of two abundant numbers. If a certain
    # number can, add it to the answer.
    for i in NumberList:
        Limit = (i // 2) + 1
        IsSumOfAbundantNumbers = False
        for j in AbundantNumbers:
            if j < Limit:
                if (i - j) in AbundantNumbers:
                    IsSumOfAbundantNumbers = True
                    break
            else:
                break
        if IsSumOfAbundantNumbers == False:
            Answer += i

    # Print the answer, the sum of all numbers that are not the sum of
    # two abundant numbers
    print(Answer)

if __name__ == "__main__":
    main()
