#!/usr/bin/perl

# http://projecteuler.net/problem=20
#
# n! means n * (n − 1) * ... * 3 * 2 * 1
#
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 +
# 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

use Math::BigInt;

# Calculate the factorial of a number iteratively
sub Factorial {
    $Number = $_[0];
    $Factorial = 1;

    for($i = 2; $i <= $Number; $i++) {
        $Factorial = Math::BigInt->new($Factorial * $i);
    }

    return $Factorial;
}

# Get the factorial of 100 as a number and convert it to a string
$Result = Factorial(100);
$ResultString = "$Result";
$Answer = 0;

# Sum the digits of Factorial(100)
for($i = 0; $i < length($ResultString); $i++) {
    $Answer += substr($ResultString, $i, 1);
}

# Print the answer
print "$Answer\n";
