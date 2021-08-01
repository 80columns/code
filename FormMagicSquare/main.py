"""
https://www.hackerrank.com/challenges/magic-square-forming/problem
"""

def getModificationCost(sourceList, destinationList):
    cost = 0

    for x in range(0, len(sourceList)):
        if sourceList[x] != destinationList[x]:
            cost += abs(sourceList[x] - destinationList[x])

    return cost

def formMagicSquare(s):
    middle_cost = 0 if s[1][1] == 5 else abs(5 - s[1][1])
    cost = None
    final_list = [8, 3, 4, 9, 2, 7, 6, 1]
    final_list_reversed = [8, 1, 6, 7, 2, 9, 4, 3]
    outer_list = []

    for x in range(0, 3):
        outer_list.append(s[0][x])

    outer_list.append(s[1][2])

    for x in range(2, -1, -1):
        outer_list.append(s[2][x])

    outer_list.append(s[1][0])

    # find which offset from final_list and final_list_reversed has the most
    # matches with the outer numbers
    for x in range(0, len(final_list), 2):
        temp_cost = getModificationCost(outer_list, final_list[x:] + final_list[:x])

        if cost is None or temp_cost < cost:
            cost = temp_cost
    
    for x in range(0, len(final_list_reversed), 2):
        temp_cost = getModificationCost(outer_list, final_list_reversed[x:] + final_list_reversed[:x])

        if cost is None or temp_cost < cost:
            cost = temp_cost

    return cost + middle_cost

def main():
    s = [[5, 3, 4],
         [1, 5, 8],
         [6, 4, 2]]

    print(formMagicSquare(s))

if __name__ == '__main__':
    main()