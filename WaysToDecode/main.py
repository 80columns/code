"""
https://youtu.be/qli-JCrSwuk

Input:
a string of integers

Output:
how many unique strings of characters could have mapped to the string
of integers, given a mapping dictionary such as:

'a' -> 1
'b' -> 2
...
'y' -> 25
'z' -> 26

Sample input:
"12"

Sample output:
2
('ab' or 'l' could map to "12")

Assumptions:
the input string int_string will only contain the digits 1-9
"""

def num_ways(int_string, char_num_map, num_ways_map):
    if int_string in num_ways_map:
        return num_ways_map[int_string]

    if len(int_string) == 0:
        num_ways_map[int_string] = 0
    elif len(int_string) == 1:
        num_ways_map[int_string] = 1
    else:
        combined_num_ways = \
            num_ways_map[int_string[1:]] \
            if int_string[1:] in num_ways_map \
            else num_ways(int_string[1:], char_num_map, num_ways_map)

        if int(int_string[:2]) in char_num_map.values():
            combined_num_ways += \
                num_ways_map[int_string[2:]] \
                if int_string[2:] in num_ways_map \
                else num_ways(int_string[2:], char_num_map, num_ways_map)

        num_ways_map[int_string] = combined_num_ways

    print(f"num ways for '{int_string}' is {num_ways_map[int_string]}")
    return num_ways_map[int_string]

def main():
    # assume that the mapping here is 'a' -> 1, 'b' -> 2, ... 'y' -> 25,
    # 'z' -> 26, although the mapping could be arbitrary assuming there is
    # a unique mapping of letters to integers
    char_num_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
        'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
        's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }

    print(num_ways("12", char_num_map, {}))
    print(num_ways("12345", char_num_map, {}))
    print(num_ways("27345", char_num_map, {}))
    print(num_ways("111111", char_num_map, {}))

if __name__ == "__main__":
    main()