#!/usr/bin/python

'''
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''

def main():

    Sum1 = 0
    Sum2 = 0

    for I in range(1, 101):
        Sum1 += I
        Sum2 += I**2

    print(Sum1**2 - Sum2)

if __name__ == "__main__":
    main()
