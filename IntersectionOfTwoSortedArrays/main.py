"""
Input:
Two sorted arrays, a and b

Output:
The unique digits found in both a and b


Sample input:
a = [1, 2, 3, 6, 10, 11, 13, 19, 24, 25, 39, 49]
b = [-5, 0, 2, 10, 11, 12, 14, 15, 17, 25, 60]

Sample output:
[2, 10, 11, 25]


Assumptions:
The input lists may contain duplicate integers
"""

def find_sorted_array_intersection(a, b):
    a_index = 0
    b_index = 0
    intersection = []

    # use two pointers, a_index and b_index, to traverse the lists in
    # linear time
    while a_index < len(a) and b_index < len(b):
        while a_index < len(a) and a[a_index] < b[b_index]:
            a_index += 1

        if a_index == len(a):
            break

        while b_index < len(b) and b[b_index] < a[a_index]:
            b_index += 1

        if b_index == len(b):
            break

        if a[a_index] == b[b_index]:
            val = a[a_index]

            intersection.append(val)

            a_index += 1
            b_index += 1

            # skip over any duplicate items in the list
            while a_index < len(a) and a[a_index] == val:
                a_index += 1

            while b_index < len(b) and b[b_index] == val:
                b_index += 1

    return intersection

def main():
    print(find_sorted_array_intersection( \
        [1, 2, 3, 6, 10, 11, 13, 19, 24, 25, 39, 49], \
        [-5, 0, 2, 10, 11, 12, 14, 15, 17, 25, 60]) \
    )

    print(find_sorted_array_intersection( \
        [1, 2, 2, 2, 2, 2, 7, 7, 7, 25, 27], \
        [-5, 0, 2, 2, 3, 4, 5, 6, 6, 7, 25, 60]) \
    )

if __name__ == "__main__":
    main()