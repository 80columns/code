'''
Sample input:
101,5,87,567,90,6,10,82,405,15,520,30,16,10,7,167,25,99

Sample output:
[5, 6, 7, 10, 10, 15, 16, 25, 30, 82, 87, 90, 99, 101, 167, 405, 520, 567]
'''

import sys

def main():
    try:
        if len(sys.argv) != 2:
            print(f'\nError: input numbers specified in an invalid format')
            raise ValueError

        numbers = [int(x) for x in sys.argv[1].split(',')]

        LinearSort(numbers)

        print(numbers)
        
    except:
        print('\nUsage: specify a comma-separated list of numbers to sort, e.g.:')
        print('python main.py 101,5,87,567,90,6,10,82,405,15,520,30,16,10,7,167,25,99\n')

def LinearSort(numbers):
    smallest = largest = numbers[0]
    lookup = {}
    index = 0

    for x in range(0, len(numbers)):
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