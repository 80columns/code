"""
https://projecteuler.net/problem=41
"""

import math
from itertools import permutations

def isPrime(number):
    if number % 2 == 0:
        return False

    root = math.floor(math.sqrt(number))

    for x in range(3, root, 2):
        if number % x == 0:
            return False

    return True

def generatePandigitals():
    for l in range(10, 3, -1):
        print(f"checking with l = {l}...")
        pandigitals = list(permutations(range(1, l)))
        pandigitals.reverse()

        for p in pandigitals:
            number = int("".join([str(x) for x in p]))

            if isPrime(number):
                return number

    return None

def main():
    print(generatePandigitals())

if __name__ == "__main__":
    main()