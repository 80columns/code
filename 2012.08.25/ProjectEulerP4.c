/*
 * http://projecteuler.net/problem=4
 *
 * A palindromic number reads the same both ways. The largest
 * palindrome made from the product of two 2-digit numbers is
 * 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit
 * numbers.
 *
 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* This function determines whether an integer is a palindrome
 * by reversing it and comparing the original to the reversed
 * integer */
int IsPalindrome(int Integer) {
    int Reverse = 0, Temp = Integer;

    /* Reverse Integer */
    while(Temp != 0) {
        Reverse *= 10;
        Reverse += Temp % 10;
        Temp /= 10;
    }

    /* Return true / false */
    if(Reverse == Integer) {
        return 1;
    }
    else {
        return 0;
    }
}

int main() {
    int I = 0, J = 0, Product = 0, LargestPalindrome = 0;
    int* Palindromes = NULL;
    int ArraySize = 0;

    /* Get the palindromes that are products of numbers between
     * 100 and 999 */
    for(I = 999; I > 99; I--) {
        for(J = 999; J > 99; J--) {
            Product = I * J;

            if(IsPalindrome(Product) == 1) {
                ArraySize++;
                Palindromes = (int*)realloc(Palindromes, ArraySize \
                                            * sizeof(int));
                Palindromes[ArraySize - 1] = Product;
            }
        }
    }

    /* Get the largest palindrome out of the array */
    LargestPalindrome = Palindromes[0];
    for(I = 1; I < ArraySize; I++) {
        if(Palindromes[I] > LargestPalindrome) {
            LargestPalindrome = Palindromes[I];
        }
    }

    /* Print the answer */
    printf("%d\n", LargestPalindrome);

    /* Free the dynamic array used to store the palindromes */
    free(Palindromes);

    return 0;
}
