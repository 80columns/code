#!/usr/bin/python

# https://www.hackerrank.com/challenges/richie-rich/problem

def highestValuePalindrome(s: str, n: int, k: int):
    start = 0
    middle = n // 2
    required_changes = 0
    change_values_indices: dict[str, set[int]] = {}
    indicies_changed: set[int] = set()

    for index in range(start, middle):
        if s[index] != s[len(s) - 1 - index]:
            if s[index] not in change_values_indices:
                change_values_indices[s[index]] = set()

            change_values_indices[s[index]].add(index)
            required_changes += 1

    if required_changes > k:
        return "-1"

    for value in change_values_indices.keys():
        for index in change_values_indices[value]:
            opposite_index = len(s) - 1 - index
            new_value = max(s[index], s[opposite_index])

            indicies_changed.add(index)

            s = s[:index] + new_value + s[index+1:]
            s = s[:opposite_index] + new_value + s[opposite_index+1:]

            k -= 1

    index = start

    while k > 0 and index < middle:
        index_was_changed = index in indicies_changed

        if s[index] != '9' and ((index_was_changed and k >= 1) or (not index_was_changed and k >= 2)):
            opposite_index = len(s) - 1 - index

            s = s[:index] + '9' + s[index+1:]
            s = s[:opposite_index] + '9' + s[opposite_index+1:]

            k -= 1 if index_was_changed else 2

        index += 1

    # if there is at least one change remaining and the string has an odd number of characters,
    # replace the middle number with a 9
    if k > 0 and len(s) % 2 == 1:
        s = s[:middle] + '9' + s[middle+1:]

    return s


def main():
    '''
    s is a string of digits
    n is the length of s
    k is the maximum number of changes allowed
    '''

    print(highestValuePalindrome(s="1231", n=4, k=3)) # output should be 9339
    print(highestValuePalindrome(s="12321", n=5, k=1)) # output should be 12921
    print(highestValuePalindrome(s="3943", n=4, k=1)) # output should be 3993
    print(highestValuePalindrome(s="092282", n=6, k=3)) # output should be 992299
    print(highestValuePalindrome(s="0011", n=4, k=1)) # output should be -1


if __name__ == "__main__":
    main()
