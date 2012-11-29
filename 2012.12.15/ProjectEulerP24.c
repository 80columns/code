/*
 * http://projecteuler.net/problem=24
 *
 * A permutation is an ordered arrangement of objects. For example,
 * 3124 is one possible permutation of the digits 1, 2, 3 and 4. If
 * all of the permutations are listed numerically or alphabetically,
 * we call it lexicographic order. The lexicographic permutations of
 * 0, 1 and 2 are:
 *
 *              012   021   102   120   201   210
 *
 * What is the millionth lexicographic permutation of the digits 0, 1,
 * 2, 3, 4, 5, 6, 7, 8 and 9?
 *
 */

#include <stdio.h>

/* As C's math library doesn't have a power function for integers,
 * here is a simple one.
 */
unsigned long long int IntPow(int Base, int Exponent) {
    int i = 0;
    unsigned long long int Pow = 1;

    for(i = 0; i < Exponent; i++) {
        Pow *= Base;
    }

    return Pow;
}

/* Get the factorial of Integer */
int Factorial(int Integer) {
    int Result = 2;
    int i = 0;

    if(Integer == 1 || Integer == 2) {
        return Integer;
    }
    else {
        for(i = 3; i <= Integer; i++) {
            Result *= i;
        }

        return Result;
    }
}

/* This function returns the Nth lexicographic permutation of the
 * digits in Digits[].
 */
unsigned long long int GetLexicographicPermutation(int Digits[], \
                                                 int NumDigits, \
                                                 int N) {
    unsigned long long int NthPermutation = 0;
    int Index = 0;
    int Fact = 0;
    int i = 0;
    int j = 0;
    int k = 0;

    /* Starting at the leftmost position in the permutation, calculate
     * which digit belongs at that position by determining how many
     * possible combinations there are after a digit has been chosen
     * for that position. Then, based on the number of combinations
     * and N, calculate which digit would iterate over the most number
     * of permutations before going over N. Do this iteratively from
     * left to right until each position has been filled with a digit.
     */
    for(i = (NumDigits - 1); i >= 0; i--) {
        Fact = Factorial(i);
        j = 0;
        
        while(Fact < N) {
            N -= Fact;
            j++;
        }

        for(k = 0; k <= j; k++) {
            if(Digits[k] == -1) {
                j++;
            }
        }

        NthPermutation += Digits[j] * IntPow(10, i);
        Digits[j] = -1;
    }

    return NthPermutation;
}

int main() {
    int Digits[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int NumDigits = sizeof(Digits) / sizeof(int);
    int N = 1000000;
    unsigned long long int Answer = 0;

    Answer = GetLexicographicPermutation(Digits, NumDigits, N);

    /* Print the answer */
    printf("%llu\n", Answer);

    return 0;
}
