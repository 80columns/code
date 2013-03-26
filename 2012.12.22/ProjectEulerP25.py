#!/usr/bin/python3

'''
http://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000
digits?
'''

from sys import exit

def Fibonacci(Number):

    Previous = 0
    Current = 1
    Result = 0

    i = 2

    while i <= Number:
        Result = Previous + Current
        Previous = Current
        Current = Result

        i += 1

    return Result

def IsFirstWithNDigits(Number):

    if len(str(Fibonacci(Number))) == len(str(Fibonacci(Number-1))):
        return False
    else:
        return True

def FindFirstWithNDigits(n, x):
    z = 0

    while(IsFirstWithNDigits(n * 4 + x - z)) == False:
        z += 1

    print(n * 4 + x - z)

def main():

    Max = 1000
    n = 5
    x = 1
    i = 0

    # Fib(21) is the first fibonacci number with 5 digits
    # The formula n * 4 + x (where x is determined by a pattern)
    # determines the first fibonacci number with n digits; that is
    # until n = 46. The formula then irregularly produces numbers that
    # are greater than the first fibonacci number with n digits. This
    # divergence is slow, however. For example, when n = 1000,
    # x = 783. (1000 * 4) + 783 = 4783. However, 4782 is the first
    # Fibonacci number with 1000 digits. Any value produced by the
    # function for n <= 1000 is only off by +1. For n <= 2000, the
    # possible values rise sequentially; when n = 2000, x = 1569.
    # (2000 * 4) + 1569 = 9569. The first Fibonacci number with 2000
    # digits is 9567; so the formula is only off by +2 here. My
    # assumption is that the difference slowly rises as n and x grow
    # larger.
    while 1:
        if n == Max:
            FindFirstWithNDigits(n, x)
            exit(0)

        if i % 3 == 0:
            i = 0

            for j in range(1, 4):
                n += 1
                x += 1
                if n == Max:
                    FindFirstWithNDigits(n, x)
                    exit(0)
            n += 1
        
        else:
            for j in range(1, 5):
                n += 1
                x += 1
                if n == Max:
                    FindFirstWithNDigits(n, x)
                    exit(0)
            n += 1

        i += 1;

if __name__ == "__main__":
    main()
