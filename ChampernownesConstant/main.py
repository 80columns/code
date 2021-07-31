"""
https://projecteuler.net/problem=40

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

d1 = 1
d10 = 1
d100 = 5

0.12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455...
  ^        ^                                                                                         ^
  1        10                                                                                        100
"""

import math

def get_digit_at_index(index):
    sum = 1
    width = 1
    next_width_sum = 10**(width-1) * 9

    while (sum + (next_width_sum * width)) < index:
        sum += next_width_sum * width
        width += 1
        next_width_sum = 10**(width-1) * 9

    first_number_with_width = 10**(width-1)

    target_number = ((index - sum) // width) + first_number_with_width
    target_number_index = (index - sum) % width

    # get the digit in target_number at target_number_index
    target_number_width = math.floor(math.log10(target_number))

    while target_number_width > target_number_index:
        target_number //= 10
        target_number_width -= 1

    return target_number % 10

def main():
    # d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    print(get_digit_at_index(1)
        * get_digit_at_index(10)
        * get_digit_at_index(100)
        * get_digit_at_index(1000)
        * get_digit_at_index(10000)
        * get_digit_at_index(100000)
        * get_digit_at_index(1000000))

if __name__ == "__main__":
    main()