#!/usr/bin/php

<?php

    /*
     * http://projecteuler.net/problem=7
     *
     * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
     * we can see that the 6th prime is 13.
     *
     * What is the 10,001st prime number?
     *
     */

    /* This function determines if an odd integer is prime */
    function IsPrime($Integer) {

        /* Check if the number is divisible by 3 */
        if($Integer % 3 == 0) {
            return false;
        }

        /* If the integer is not prime, at least one of its factors
         * must be less than or equal to its square root */
        $Limit = floor(sqrt($Integer));

        for($I = 5; $I <= $Limit; $I += 2) {
            if($Integer % $I == 0) {
                return false;
            }
        }

        return true;
    }

    /* Start with the 6th prime */
    $J = 13;

    /* Iterate until we have the 10001st prime */
    for($I = 6; $I < 10001; ) {
        $J += 2;

        if(IsPrime($J)) {
            $I++;
        }
    }

    /* Print the answer */
    echo "$J\n";

?>
