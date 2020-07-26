'''
Sample input:
101,87,5,567,90

Sample output:
[5, 87, 90, 101, 567]
'''

import sys

def main():
    try:
        if len(sys.argv) != 2:
            print(f'\nError: invalid input format')
            raise ValueError

        numbers = [int(x) for x in sys.argv[1].split(',')]

        LinearSort(numbers)
        print(numbers)
        
    except:
        print('\nUsage: pass a comma-separated number list, e.g.:')
        print('python main.py 101,87,5,567,90\n')

def LinearSort(numbers):
    smallest = largest = numbers[0]
    lookup = {numbers[0]:1}
    index = 0

    for x in range(1, len(numbers)):
        if numbers[x] in lookup:
            lookup[numbers[x]] += 1
        else:
            lookup[numbers[x]] = 1

        if numbers[x] < smallest:
            smallest = numbers[x]
        elif numbers[x] > largest:
            largest = numbers[x]

    for x in range(smallest, largest + 1):
        if x in lookup:
            for y in range(0, lookup[x]):
                numbers[index] = x
                index += 1

if __name__ == "__main__":
    main()