"""
https://www.youtube.com/watch?v=4eWKHLSRHPY
Input:
    an array of integers sorted in ascending order
Output:
    an array of the squares of the integers from the input array, sorted
    in ascending order

Sample input:
    [-6, -4, 1, 2, 3, 5]
Sample output:
    [1, 4, 9, 16, 25, 36]
"""

def main():
    # no negative or positive
    print(sort_squared([0, 0, 0]))
    # [0, 0, 0]

    # all negative
    print(sort_squared([-10, -5, -3, -2, -1]))
    # [1, 4, 9, 25, 100]

    # all positive
    print(sort_squared([10, 24, 32, 54, 77, 89]))
    # [100, 576, 1024, 2916, 5929, 7921]

    # some negative, some positive
    print(sort_squared([-6, -4, 1, 2, 3, 5]))
    # [1, 4, 9, 16, 25, 36]

    # some zero, some positive
    print(sort_squared([0, 0, 5, 10, 15, 20]))
    # [0, 0, 25, 100, 225, 400]

    # some negative, some zero
    print(sort_squared([-16, -8, -4, -2, 0, 0, 0]))
    # [0, 0, 0, 4, 16, 64, 256]

    # some negative, some zero, some positive
    print(sort_squared([-20, -10, -5, -2, 0, 0, 0, 3, 7, 11, 13]))
    # [0, 0, 0, 4, 9, 25, 49, 100, 121, 169, 400]

def sort_squared(arr):
    # determine in O(1) time if all the input numbers are negative
    if arr[-1] < 0:
        # if the last number in the array is negative, then all of them are
        out_arr = []

        for x in range(len(arr) - 1, -1, -1):
            out_arr.append(arr[x]**2)

        return out_arr

    # determine in O(1) time if all the input numbers are non-negative
    elif arr[0] > -1:
        # if the first number in the array is positive, then all of them are
        for x in range(0, len(arr)):
            arr[x] = arr[x]**2

        return arr

    else:
        # some negative and some non-negative numbers exist in arr
        start = 0
        end = len(arr) - 1
        out_arr = []

        while start < end:
            if arr[start] < 0 and (arr[start] * -1) > arr[end]:
                out_arr.insert(0, arr[start]**2)
                start += 1
            else:
                out_arr.insert(0, arr[end]**2)
                end -= 1

        out_arr.insert(0, arr[start]**2)

        return out_arr

if __name__ == "__main__":
    main()