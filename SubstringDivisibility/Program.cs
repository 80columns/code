using System;
using System.Collections.Generic;
using System.Text;

// https://projecteuler.net/problem=43

namespace SubstringDivisibility {
    class Program {
        static void Main(
            string[] args
        ) {
            var PandigitalNumberSum = 0L;
            var Digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            var PandigitalNumbers = GeneratePandigitals(Digits, 0);

            foreach (var Number in PandigitalNumbers) {
                if (
                    Convert.ToInt32(Number.Substring(startIndex: 1, length: 3)) % 2 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 2, length: 3)) % 3 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 3, length: 3)) % 5 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 4, length: 3)) % 7 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 5, length: 3)) % 11 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 6, length: 3)) % 13 == 0
                 && Convert.ToInt32(Number.Substring(startIndex: 7, length: 3)) % 17 == 0
                ) {
                    PandigitalNumberSum += Convert.ToInt64(Number);
                }
            }

            Console.WriteLine(PandigitalNumberSum);
        }

        static List<string> GeneratePandigitals(
            List<int> digits,
            int startIndex
        ) {
            var Permutations = new List<string>();

            if (startIndex == digits.Count - 1) {
                if (digits[0] != 0) {
                    var Output = new StringBuilder();

                    for (var i = 0; i < digits.Count; i++) {
                        Output.Append(digits[i]);
                    }

                    Permutations.Add(Output.ToString());
                }
            } else {
                for (var i = startIndex; i < digits.Count; i++) {
                    Permutations.AddRange(GeneratePandigitals(digits, startIndex + 1));

                    var Temp = digits[startIndex];
                    digits.RemoveAt(startIndex);
                    digits.Add(Temp);
                }
            }

            return Permutations;
        }
    }
}