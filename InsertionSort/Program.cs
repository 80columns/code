/*
 * Sample input:
 * 1,8,8,73,0,12,2348,92,83
 *
 * Sample output:
 * 0,1,8,8,12,73,83,92,2348 
 */

using System;
using System.Linq;

namespace InsertionSort {
    class Program {
        static void Main(string[] args) {
            try {
                if (args.Length != 1) {
                    PrintError();
                } else {
                    var Input = args[0].Split(",").Select(i => Convert.ToInt64(i)).ToArray();
                    Sort(Input);

                    Console.WriteLine(string.Join(",", Input));
                }
            }
            catch (Exception) {
                PrintError();
            }
        }

        static void PrintError() {
            Console.WriteLine("Error: this program can be run by specifying a single argument as a list of comma-separated numbers");
            Console.WriteLine(".\\insertionsort.exe '1,8,8,73,0,12,2348,92,83'");
        }

        static void Sort(long[] Input) {
            for (var i = 1; i < Input.Length; i++) {
                for (var j = i; j > 0 && Input[j] < Input[j - 1]; j--) {
                    var Swap = Input[j];
                    Input[j] = Input[j - 1];
                    Input[j - 1] = Swap;
                }
            }
        }
    }
}