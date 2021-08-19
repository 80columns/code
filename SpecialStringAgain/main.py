"""
https://www.hackerrank.com/challenges/special-palindrome-again/problem
"""

def countSpecialSubstrings(s):
    singleCharSubstrings = list(s)
    specialSubstrings = 0

    for i in range(0, len(s) - 1):
        # find a substring of identical characters
        j = i + 1

        if j < len(s) and s[j] == s[i]:
            while j < len(s) and s[j] == s[i]:
                # loop while the subsequent characters are identical
                specialSubstrings += 1
                j += 1

            # after the first non-identical subsequent character, mark it as a
            # potential middle index for a palindrome special substring
            middle_char_index = j
            j += 1

            if j < len(s) and s[j] == s[i]:
                while j < len(s) \
                    and s[j] == s[i] \
                    and j <= middle_char_index + (middle_char_index - i):
                    j += 1

                # if the length of the matching characters found after the
                # middle character is equal to the length of the matching
                # characters before the middle character, then we've found a
                # palindrome special substring
                if (j - 1) - middle_char_index == middle_char_index - i:
                    specialSubstrings += 1
        elif j + 1 < len(s) and s[j + 1] == s[i]:
            # if the character directly after index i (i.e. j) is different but
            # the next character is identical, then this is a 3-character
            # palindrome
            specialSubstrings += 1

    return len(singleCharSubstrings) + specialSubstrings

def main():
    print(countSpecialSubstrings("mnonopoo")) # 12
    print(countSpecialSubstrings("asasd")) # 7
    print(countSpecialSubstrings("abcbaba")) # 10 
    print(countSpecialSubstrings("aaaa")) # 10

if __name__ == "__main__":
    main()