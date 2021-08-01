"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""

def sortNumbers(a):
    min = a[0]
    max = a[0]
    num_counts = { a[0]: 1 }

    for x in a[1:]:
        if x < min:
            min = x
        elif x > max:
            max = x

        if x in num_counts:
            num_counts[x] += 1
        else:
            num_counts[x] = 1

    a_index = 0

    for x in range(min, max + 1):
        if x in num_counts:
            for _ in range(0, num_counts[x]):
                a[a_index] = x
                a_index += 1

def pickNumbers(a):
    sortNumbers(a)

    current_number = a[0]
    tracking_subarray = False
    current_subarray_length = 0
    max_subarray_length = 0

    for x in range(1, len(a)):
        if tracking_subarray is False and a[x] <= current_number + 1:
            tracking_subarray = True
            current_subarray_length = 2
        elif tracking_subarray is True and a[x] <= current_number + 1:
            current_subarray_length += 1
        elif tracking_subarray is True and a[x] > current_number + 1:
            tracking_subarray = False
            current_number = a[x]

            if current_subarray_length > max_subarray_length:
                max_subarray_length = current_subarray_length
        else:
            current_number = a[x]

    if tracking_subarray is True and current_subarray_length > max_subarray_length:
        max_subarray_length = current_subarray_length

    return max_subarray_length

def main():
    print(pickNumbers([1, 2, 2, 3, 1, 2]))
    print(pickNumbers([4, 6, 5, 3, 3, 1]))
    print(pickNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))

if __name__ == "__main__":
    main()