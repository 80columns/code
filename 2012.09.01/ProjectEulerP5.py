#!/usr/bin/python

'''
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''

def main():

    # Start at 20
    I = 20

    while 1:
        # Increment by the largest factor
        I += 20

        # The answer must be divisible by 1 through 20:
        # We can factor out 1 trivially
        # We can factor out 2 because 20 % 2 = 0
        # We can factor out 3 because 18 % 3 = 0
        # We can factor out 4 because 20 % 4 = 0
        # We can factor out 5 because 20 % 5 = 0
        # We can factor out 6 because 18 % 6 = 0
        # We can factor out 7 because 14 % 7 = 0
        # We can factor out 8 because 16 % 8 = 0
        # We can factor out 9 because 18 % 9 = 0
        # We can factor out 10 because 20 % 10 = 0
        # We can factor out 12 because (20 * 18) % 12 = 0
        # We can factor out 15 because (20 * 18) % 15 = 0
        if I % 11 == 0 and I % 13 == 0 and I % 14 == 0 \
            and I % 16 == 0 and I % 17 == 0 and \
            I % 18 == 0 and I % 19 == 0 and I % 20 == 0:
                print(I)
                break

if __name__ == "__main__":
    main()
