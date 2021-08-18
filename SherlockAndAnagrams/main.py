"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

def nChooseTwo(n):
    return (n * (n - 1)) // 2

def sherlockAndAnagrams(inputString):
    anagrams = {}
    anagramPairCount = 0

    for i in range(0, len(inputString)):
        for j in range(i + 1, len(inputString) + 1):
            letters = list(inputString[i:j])
            letters.sort()
            lettersStr = "".join(letters)

            if lettersStr in anagrams:
                anagrams[lettersStr] += 1
            else:
                anagrams[lettersStr] = 1

    for x in anagrams:
        if anagrams[x] >= 2:
            anagramPairCount += nChooseTwo(anagrams[x])

    return anagramPairCount

def main():
    print(sherlockAndAnagrams("abba")) # 4
    print(sherlockAndAnagrams("abcd")) # 0
    print(sherlockAndAnagrams("ifailuhkqq")) # 3
    print(sherlockAndAnagrams("kkkk")) # 10
    print(sherlockAndAnagrams("cdcd")) # 5

if __name__ == "__main__":
    main()