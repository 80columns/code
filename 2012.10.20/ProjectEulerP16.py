#!/usr/bin/python

'''
http://projecteuler.net/problem=16

2^15 = 32768 and the Answer of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the Answer of the digits of the number 2^1000?
'''

def main():
    # Calculate 2^1000
    NumberString = str(2**1000)
    Answer = 0

    # Add the digits in 2^1000
    for i in NumberString:
        Answer += int(i)

    # Print the answer
    print(Answer)

if __name__ == "__main__":
    main()
