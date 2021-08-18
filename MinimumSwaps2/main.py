"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""

def minSwaps(arr):
    positions = {}
    swapCount = 0

    for i in range(0, len(arr)):
        positions[arr[i]] = i

    for i in range(1, len(arr) + 1):
        if arr[i - 1] != i:
            tempVal = arr[i - 1]
            arr[i - 1] = i

            positions[tempVal] = positions[i]
            positions.pop(i)

            arr[positions[tempVal]] = tempVal

            swapCount += 1

    return swapCount

def main():
    print(minSwaps([3, 2, 1]))
    print(minSwaps([7, 1, 3, 2, 4, 5, 6]))
    print(minSwaps([4, 3, 1, 2]))
    print(minSwaps([2, 3, 4, 1, 5]))
    print(minSwaps([1, 3, 5, 2, 4, 6, 7]))

if __name__ == "__main__":
    main()