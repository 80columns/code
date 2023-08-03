/*
 * Sample input:
 * 29,8,56,0,17,5,10,31,1,40
 *
 * Sample output:
 * [0,1,5,8,10,17,29,31,40,56]
 */

using System;
using System.Linq;

namespace Heapsort {
    class Program {
        static void Main(string[] args) {
            try {
                if (args.Length != 1) {
                    PrintError("Invalid number of arguments", true);
                } else {
                    var Input = args[0].Split(",")
                                       .Select(i => Convert.ToInt64(i))
                                       .ToArray();
                    Sort(Input);
 
                    Console.WriteLine($"[{string.Join(",", Input)}]");
                }
            }
            catch (Exception e) {
                PrintError(e.Message);
            }
        }
 
        static void PrintError(
            string Message,
            bool Print_Usage = false
        ) {
            Console.WriteLine($"Error: {Message}");

            if (Print_Usage == true) {
                Console.WriteLine("This program can be run by specifying a"
                                + " single argument as a list of"
                                + " comma-separated numbers");
                Console.WriteLine(".\\heapsort.exe "
                                + " '29,8,56,0,17,5,10,31,1,40'");
            }
        }

        static void Sort(long[] Input) {
            Heapify(Input);

            for (var i = 1; i < Input.Length; i++) {
                Swap(Input, 0, Input.Length - i);
                SiftDown(Input, Input.Length - i);
            }
        }

        // create a max-heap from the input array
        static void Heapify(long[] Input) {
            var i = 0;
            var Swapped = false;

            // starting from the top of the heap, compare the value
            // of each node with its children until the last node
            // with children is reached
            while (2*i + 1 < Input.Length) {
                if (
                    2*i + 2 < Input.Length
                 && Input[2*i + 2] > Input[2*i + 1]
                 && Input[2*i + 2] > Input[i]
                ) {
                    // right node is greater than both the left node
                    // and the parent node
                    Swapped = Swap(Input, i, 2*i + 2);
                } else if (Input[2*i + 1] > Input[i]) {
                    // right node is less than the left node
                    // or doesn't exist, left node is greater
                    // than the parent node
                    Swapped = Swap(Input, i, 2*i + 1);
                } else {
                    // parent node is greater than the left node
                    // and the right node if it exists
                    Swapped = false;
                }

                // if the value of the node at index i was changed
                // via swap, process the node's parent next to
                // determine if this node's new value is greater
                // than the parent node's value
                //
                // if the node at index i was swapped but is the
                // parent node (meaning i = 0), then
                // re-processing the parent node again is redundant
                // so we move to the next node in this case
                i = (Swapped && i != 0) ? (i - 1) / 2 : i + 1;
            }
        }

        // sift the value at the top of the heap down to
        // restore the max-heap property
        static void SiftDown(
            long[] Input,
            int Limit
        ) {
            var i = 0;

            while (2*i + 1 < Limit) {
                if (
                    2*i + 2 < Limit
                 && Input[2*i + 2] > Input[2*i + 1]
                 && Input[2*i + 2] > Input[i]
                ) {
                    // right node is greater than both the left node
                    // and the parent node
                    Swap(Input, i, 2*i + 2);
                    i = 2*i + 2;
                } else if (Input[2*i + 1] > Input[i]) {
                    // right node is less than the left node
                    // or doesn't exist, left node is greater
                    // than the parent node
                    Swap(Input, i, 2*i + 1);
                    i = 2*i + 1;
                }
                else {
                    // the value of this node is greater than both
                    // the left node and right node, so the max
                    // heap property has been restored
                    break;
                }
            }
        }

        static bool Swap(
            long[] Input,
            int Index1,
            int Index2
        ) {
            var Swap = Input[Index1];
            Input[Index1] = Input[Index2];
            Input[Index2] = Swap;
            
            return true;
        }
    }
}