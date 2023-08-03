/*
 * Sample input:
 * 1,8,8,73,0,12,2348,92,83
 *
 * Sample output:
 * 0,1,8,8,12,73,83,92,2348 
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace Quicksort {
    class Program {
        static void Main(string[] args) {
            try {
                if (args.Length != 1) {
                    PrintError();
                } else {
                    var Input = args[0].Split(",").Select(i => Convert.ToInt64(i)).ToList();
                    var Output = Sort(Input);

                    Console.WriteLine(string.Join(",", Output));
                }
            }
            catch (Exception) {
                PrintError();
            }
        }

        static void PrintError() {
            Console.WriteLine("Error: this program can be run by specifying a single argument as a list of comma-separated numbers");
            Console.WriteLine(".\\quicksort.exe '1,8,8,73,0,12,2348,92,83'");
        }

        static List<long> Sort(List<long> Input) {
            if (Input.Count < 2) {
                return Input;
            } else {
                var Middle_Index = Input.Count / 2;
                var Left = Input.Where(i => i < Input[Middle_Index]).ToList();
                var Middle = Input.Where(i => i == Input[Middle_Index]).ToList();
                var Right = Input.Where(i => i > Input[Middle_Index]).ToList();

                return Sort(Left).Concat(Middle).Concat(Sort(Right)).ToList();
            }
        }
    }
}