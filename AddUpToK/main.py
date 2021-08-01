"""
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def numbers_add_up_to_k(numbers, k):
    number_set = set(numbers)

    for x in number_set:
        if k - x in number_set:
            return True

    return False

def main():
    print(numbers_add_up_to_k([10, 15, 3, 7], 17))
    print(numbers_add_up_to_k([10, 19, 3, 7, 90, 9, 23, 1, 0, 55, 6], 42))
    print(numbers_add_up_to_k([14, 13, 12, 11, 10, 9, 8], 15))

if __name__ == "__main__":
    main()