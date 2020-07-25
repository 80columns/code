'''
Sample input:
1d10 2d20 3d4 6d12

Sample output:

1d10
5

2d20
4
6

3d4
1
3
2

6d12
10
3
2
4
6
7
'''

import sys
import secrets

def main():
    try:
        if len(sys.argv) == 1:
            print(f'\nError: no dice specified to roll')
            raise ValueError

        for x in range(1, len(sys.argv)):
            Roll(sys.argv[x].split('d'))
    except:
        print('\nUsage: specify any number of dice with roll count, e.g.:')
        print('python main.py 1d10 2d4')
        print('\nValid dice are d4, d6, d8, d10, d12, d20, d100')

def Roll(roll_count_die):
    roll_count = int(roll_count_die[0])
    die = int(roll_count_die[1])

    if die not in [4, 6, 8, 10, 12, 20, 100]:
        print(f'\nError: d{die} is not a valid D&D die')
        raise ValueError

    print(f'\n{roll_count}d{die}')

    for x in range(0, roll_count):
        roll = secrets.randbelow(die) + 1

        print(roll)

if __name__ == "__main__":
    main()