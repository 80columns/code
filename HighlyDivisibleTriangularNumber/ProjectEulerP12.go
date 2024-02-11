/*
 * http://projecteuler.net/problem=12
 *
 * The sequence of triangle numbers is generated by adding the natural
 * numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6
 * + 7 = 28. The first ten terms would be:
 *
 *     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
 *
 * Let us list the factors of the first seven triangle numbers:
 *
 *    1: 1
 *    3: 1,3
 *    6: 1,2,3,6
 *   10: 1,2,5,10
 *   15: 1,3,5,15
 *   21: 1,3,7,21
 *   28: 1,2,4,7,14,28
 *
 * We can see that 28 is the first triangle number to have over five
 * divisors.
 *
 * What is the value of the first triangle number to have over five
 * hundred divisors?
 *
 */

package main

import (
    "math"
    "fmt"
)

func CountDivisors(Integer float64) int {
    /* Only count divisors up to the square root of Integer */
    var Limit float64 = math.Floor(math.Sqrt(Integer))
    var I float64 = 0

    /* Every number is divisible by itself and 1 */
    var NumDivisors int = 2

    if math.Mod(Integer, 2) == 0 {
        /* If the number is even, it's divisible by 2 and some other
         * number */
        NumDivisors += 2

        /* Start checking the number's divisibility from 3 */
        I = 3

        /* Check the number's divisibility for all integers from 3 up
         * to it's square root */
        for I <= Limit {
            /* If we find a divisor, the number that we can multiply
             * it by to get Integer is also a divisor, so increment
             * by 2 as we are only checking up to the number's square
             * root */
            if math.Mod(Integer, I) == 0 {
                NumDivisors += 2
            }

            /* Increment by 1 as an even number can have both odd and
             * even divisors */
            I += 1
        }

    } else {
        /* Start checking the number's divisibility from 3 */
        I = 3

        for I <= Limit {
            /* If we find a divisor, the number that we can multiply
             * it by to get Integer is also a divisor, so increment
             * by 2 as we are only checking up to the number's square
             * root */
            if math.Mod(Integer, I) == 0 {
                NumDivisors += 2
            }

            /* Increment by 2 so that we only check odd divisors */
            I += 2
        }
    }

    return NumDivisors
}

func main() {
    /* Start with the 8th triangle number */
    var I float64 = 8
    var NumDivisors int = 0
    var TriangleNumber float64 = 28

    /* Loop over every triangle number until we find the first
     * one with more than 500 divisors */
    for true {
        TriangleNumber += I

        NumDivisors = CountDivisors(TriangleNumber)

        if NumDivisors > 500 {
            break
        }

        I += 1
    }

    /* Print the answer */
    fmt.Println(TriangleNumber)

    return
}