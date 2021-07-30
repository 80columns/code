"""
https://youtu.be/jZBnFxIe4Y8

Input:
An order of letters in an alient alphabet
A list of words written in the alien language

Output:
True if the list of words is sorted lexicographically according to the order of
the letters in the alien alphabet, otherwise False


Sample input:
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

Sample output:
True

Sample input:
words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

Sample output:
False

Sample input:
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

Sample output:
False

Assumptions:
The list of words should be ordered in ascending order
"""

def is_ordered_lexicographically(words, order):
    letter_positions = {}
    ordered = True

    # create a reverse mapping of the letter to its position in the alphabet
    x = 0

    for letter in order:
        letter_positions[letter] = x
        x += 1

    for y in range(0, len(words) - 1):
        print(f"checking {words[y]} against {words[y + 1]}")

        # check this word against the next word
        word_1_len = len(words[y])
        word_2_len = len(words[y + 1])

        word_1_index = 0
        word_2_index = 0

        while word_1_index < word_1_len \
          and word_2_index < word_2_len:
            if letter_positions[words[y][word_1_index]] == letter_positions[words[y + 1][word_2_index]]:
                word_1_index += 1
                word_2_index += 1
            else:
                if letter_positions[words[y][word_1_index]] > letter_positions[words[y + 1][word_2_index]]:
                    ordered = False

                break

        if word_2_index == word_2_len \
       and word_1_len > word_2_len:
            # if word 1 is longer than word 2, and the entire word 2 matches a
            # prefix of word 1, then word 1 is considered "greater" than word 2
            # because the remainig characters of word 2 are considered as empty
            # spaces
            ordered = False

        if not ordered:
            # stop checking words if an unordered pair is detected
            break

    return ordered

def main():
    print(is_ordered_lexicographically(["hello", "leetcode"],    "hlabcdefgijkmnopqrstuvwxyz"))
    print(is_ordered_lexicographically(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
    print(is_ordered_lexicographically(["apple", "app"],         "abcdefghijklmnopqrstuvwxyz"))

    # worst-case
    # n = the count of words in the input list
    # m = the average length of the words in the input list
    # O(n * m)
    print(is_ordered_lexicographically(["aaaaa", "aaaaaaa", "aaaaaaaaa", "aaaaaaaaa"], "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()