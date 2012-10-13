/*
 * http://projecteuler.net/problem=17
 *
 * If the numbers 1 to 5 are written out in words: one, two, three,
 * four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used
 * in total.
 *
 * If all the numbers from 1 to 1000 (one thousand) inclusive were
 * written out in words, how many letters would be used?
 *
 *
 * NOTE: Do not count spaces or hyphens. For example, 342 (three
 * hundred and forty-two) contains 23 letters and 115 (one hundred and
 * fifteen) contains 20 letters. The use of "and" when writing out
 * numbers is in compliance with British usage.
 */

using System;

class ProjectEulerP17 {
    static int Main() {
        /* Create string arrays containing the necessary names
         * needed to represent the numbers 1 to 999
         */
        string[] OnesNames =
            new string[] {"", "one", "two", "three", "four", "five",
                          "six", "seven", "eight", "nine"};
        string[] TeensNames =
            new string[] {"ten", "eleven", "twelve", "thirteen",
                          "fourteen", "fifteen", "sixteen",
                          "seventeen", "eighteen", "nineteen"};
        string[] TensNames =
            new string[] {"twenty", "thirty", "forty", "fifty",
                          "sixty", "seventy", "eighty", "ninety"};

        /* HundredPrefixLength will be set to the length of the string
         * "Xhundredand" where X is the current multiple of 100
         */
        int HundredPrefixLength = 0;
        int Answer = 0;

        for(int i = 0; i < OnesNames.Length; i++) {
            /* Set HundredPrefixLength to the length of the current
             * hundreds place plus the length of the string
             * "hundredand". If the current iteration is for the
             * numbers 1-99, then set the length of
             * HundredPrefixLength to 0. If the current iteration is
             * for a multiple of 100, then add the length of the name
             * "Xhundred".
             */
            if(OnesNames[i].Length > 0) {
                HundredPrefixLength = OnesNames[i].Length + 10;
                Answer += HundredPrefixLength - 3;
            }
            else {
                HundredPrefixLength = 0;
            }

            /* Add the lengths of the names of the numbers 1-10 */
            for(int j = 1; j < OnesNames.Length; j++) {
                Answer += HundredPrefixLength +
                          OnesNames[j].Length;
            }

            /* Add the lengths of the names of the numbers 11-19 */
            for(int k = 0; k < TeensNames.Length; k++) {
                Answer += HundredPrefixLength +
                          TeensNames[k].Length;
            }

            /* Add the lengths of the names of the numbers 20-99 */
            for(int l = 0; l < TensNames.Length; l++) {
                Answer += HundredPrefixLength +
                          TensNames[l].Length;

                for(int m = 1; m < OnesNames.Length; m++) {
                    Answer += HundredPrefixLength +
                              TensNames[l].Length +
                              OnesNames[m].Length;
                }
            }
        }

        /* Add the length of "onethousand" for the last number in the
         * series
         */
        Answer += 11;

        /* Print the answer */
        Console.WriteLine(Answer);

        return 0;
    }
}
