/*
 * http://projecteuler.net/problem=1
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <iostream>

using namespace std;

int main()
{
    int I, J, Sum = 0;

    for(I = 3; I < 1000; I += 3)
    {
        /* Add all multiples of 3 that are below 1000 */
        Sum += I;
    }

    for(I = 5, J = 1; I < 1000; I += 5, J++)
    {
        /* Add all multiples of 5 that are below 1000 and that
         * are not also multiples of 3 */
        if(J % 3 != 0)
        {
            Sum += I;
        }
    }

    cout << "Answer = " << Sum << endl;

    return 0;
}
