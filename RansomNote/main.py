"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

def checkMagazine(magazine, note):
    magazineMatchesNote = True
    magazineDict = {}
    noteDict = {}

    for x in magazine:
        if x in magazineDict:
            magazineDict[x] += 1
        else:
            magazineDict[x] = 1

    for y in note:
        if y in noteDict:
            noteDict[y] += 1
        else:
            noteDict[y] = 1

    for z in noteDict:
        if z not in magazineDict or noteDict[z] > magazineDict[z]:
            magazineMatchesNote = False
            break

    print("Yes" if magazineMatchesNote == True else "No")

def main():
    checkMagazine(["give", "me", "one", "grand", "today", "night"], ["give", "one", "grand", "today"])
    checkMagazine(["two", "times", "three", "is", "not", "four"], ["two", "times", "two", "is", "four"])
    checkMagazine(["ive", "got", "a", "lovely", "bunch", "of", "coconuts"], ["ive", "got", "some", "coconuts"])

if __name__ == "__main__":
    main()