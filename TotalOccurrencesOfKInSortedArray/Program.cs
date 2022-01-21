using System;

// https://youtu.be/RlXtTF34nnE

namespace TotalOccurrencesOfKInSortedArray {
    class Program {
        static void Main(
            string[] args
        ) {
            var SortedArray = new int[] { 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7 };

            Console.WriteLine(FindTotalOccurrences(SortedArray, 1));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 2));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 3));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 4));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 5));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 6));
            Console.WriteLine(FindTotalOccurrences(SortedArray, 7));
        }

        static int FindTotalOccurrences(
            int[] sortedArray,
            int findMe
        ) {
            var FirstMatchedIndex = -1;
            var LeftmostIndex = -1;
            var RightmostIndex = -1;

            var LeftIndex = 0;
            var RightIndex = sortedArray.Length - 1;

            // look for any index of findMe in sortedArray
            while (FirstMatchedIndex == -1) {
                var MiddleIndex = LeftIndex + ((RightIndex - LeftIndex) / 2);

                if (sortedArray[MiddleIndex] > findMe) {
                    RightIndex = MiddleIndex;
                } else if (sortedArray[MiddleIndex] < findMe) {
                    LeftIndex = MiddleIndex;
                } else {
                    FirstMatchedIndex = MiddleIndex;
                    break;
                }
            }

            // look for the left-most index of findMe in sortedArray
            LeftIndex = 0;
            RightIndex = FirstMatchedIndex;

            while (LeftmostIndex == -1) {
                if (
                    RightIndex == 0
                 || (sortedArray[RightIndex] == findMe && sortedArray[RightIndex - 1] != findMe)
                ) {
                    LeftmostIndex = RightIndex;

                    break;
                }

                var MiddleIndex = LeftIndex + ((RightIndex - LeftIndex) / 2);

                if (sortedArray[MiddleIndex] == findMe) {
                    RightIndex = MiddleIndex;
                } else {
                    LeftIndex = MiddleIndex;
                }
            }

            LeftIndex = FirstMatchedIndex;
            RightIndex = sortedArray.Length - 1;

            // look for the right-most index of findMe in sortedArray
            while (RightmostIndex == -1) {
                if (
                    LeftIndex == sortedArray.Length - 1
                 || (sortedArray[LeftIndex] == findMe && sortedArray[LeftIndex + 1] != findMe)
                ) {
                    RightmostIndex = LeftIndex;

                    break;
                }

                var MiddleIndex = LeftIndex + ((RightIndex - LeftIndex) / 2);
                MiddleIndex = (MiddleIndex == LeftIndex) ? RightIndex : MiddleIndex;

                if (sortedArray[MiddleIndex] == findMe) {
                    LeftIndex = MiddleIndex;
                } else {
                    RightIndex = MiddleIndex;
                }
            }

            return (RightmostIndex - LeftmostIndex) + 1;
        }
    }
}