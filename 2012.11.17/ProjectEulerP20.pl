#!/usr/bin/perl

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
