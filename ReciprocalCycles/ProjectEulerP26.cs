/*
 * http://projecteuler.net/problem=26
 *
 * A unit fraction contains 1 in the numerator. The decimal
 * representation of the unit fractions with denominators 2 to 10 are
 * given:
 *
 * 1/2 = 0.5
 * 1/3 = 0.(3)
 * 1/4 = 0.25
 * 1/5 = 0.2
 * 1/6 = 0.1(6)
 * 1/7 = 0.(142857)
 * 1/8 = 0.125
 * 1/9 = 0.(1)
 * 1/10 = 0.1
 *
 * Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
 * It can be seen that 1/7 has a 6-digit recurring cycle.
 *
 * Find the value of d < 1000 for which 1/d contains the longest
 * recurring cycle in its decimal fraction part.
 */

using System;
using System.Text.RegularExpressions;

class ProjectEulerP26 {
    static void Main() {
        string DecimalValue = "";
        int RecurringCycleLength = 0;
        int LongestRecurringCycleLength = 0;
        int LongestRecurringCycleDenominator = 0;

        for(int i = 2; i < 1000; i++)
        {
            DecimalValue = 
                DivideWithDecimalPlaces(Convert.ToDouble(i));
            RecurringCycleLength = 
                ComputeRepeatingPatternLength(DecimalValue);

            if(RecurringCycleLength > LongestRecurringCycleLength)
            {
                LongestRecurringCycleLength = RecurringCycleLength;
                LongestRecurringCycleDenominator = i;
            }
        }

        Console.WriteLine(LongestRecurringCycleDenominator);
    }

    static int ComputeRepeatingPatternLength(string DecimalValue) {
        int RecurringCycleLength = 0;
        DecimalValue = DecimalValue.Remove(0, 2);
        Regex RegexPattern = new Regex(@"(.+?)(?=\1)");
        MatchCollection RegexPatternMatches = 
            RegexPattern.Matches(DecimalValue);

        foreach(Match RegexPatternMatch in RegexPatternMatches)
        {
            if(RegexPatternMatch.Success)
            {
                if(RegexPatternMatch.Value.Length >
                   RecurringCycleLength)
                {
                    RecurringCycleLength = 
                        RegexPatternMatch.Value.Length;
                }
            }
        }

        return RecurringCycleLength;
    }

    static string DivideWithDecimalPlaces(double Divisor) {
        string DecimalValue = "0.";
        double Dividend = 1.0;
        int NextDecimalDigit = 0;

        while(DecimalValue.Length < 2000) {
            Dividend *= 10.0;

            while (Divisor > Dividend)
            {
                Dividend *= 10.0;
                DecimalValue += "0";
            }

            NextDecimalDigit = 
                Convert.ToInt32(Math.Floor(Dividend / Divisor));
            DecimalValue += Convert.ToString(NextDecimalDigit);

            Dividend = (double)((int)Dividend % (int)Divisor);

            if(Dividend == 0.0) {
                break;
            }
        }

        return DecimalValue;
    }
}
