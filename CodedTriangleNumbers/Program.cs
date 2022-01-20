using System;
using System.Linq;
using System.IO;
using System.Threading.Tasks;

// https://projecteuler.net/problem=42

namespace CodedTriangleNumbers {
    class Program {
        static async Task Main() {
            var TriangleWordCount = 0;
            var Words = (await File.ReadAllTextAsync("p042_words.txt"))
                            .Split(',', StringSplitOptions.RemoveEmptyEntries)
                            .Select(s => s.Trim('"'))
                            .ToList();

            foreach (var Word in Words) {
                if (IsTriangleWord(Word)) {
                    TriangleWordCount++;
                }
            }

            Console.WriteLine(TriangleWordCount);
        }

        static bool IsTriangleWord(
            string word
        ) {
            var Number = GetStringNumber(word);

            return IsTriangleNumber(Number);
        }

        static int GetStringNumber(
            string word
        ) {
            var Number = 0;

            foreach (var character in word) {
                Number += ((int)character) - 64;
            }

            return Number;
        }

        static bool IsTriangleNumber(
            int number
        ) {
            /*
             * if number is a triangle number, then it can be represented as:
             *
             * number = (x^2 + x) / 2
             * => number * 2 = (x^2 + x)
             *
             * you can determine if a number is a triange number by doubling it,
             * taking the floor of its square root (n),
             * then checking if the doubled number is equal to n * (n + 1)
             *
             * e.g.
             * 1 is the 1st triangle number
             * 1 * 2 = 2
             * sqrt(2) = 1.41, floor = 1
             * 1 * 2 = 2
             *
             * 21 is the 6th triangle number
             * 21 * 2 = 42
             * sqrt(42) = 6.48, floor = 6
             * 6 * 7 = 42
             *
             * 55 is the 10th triangle number
             * 55 * 2 = 110
             * sqrt(110) = 10.49, floor = 10
             * 10 * 11 = 110
             */

            var Multiple = number * 2;
            var RootFloor = (int)Math.Floor(Math.Sqrt(Multiple));

            return (Multiple == RootFloor * (RootFloor + 1));
        }
    }
}