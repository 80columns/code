import sys
import secrets

def main():
    if len(sys.argv) != 3:
        print('Error: specify die (d4,d6,d8,d10,d12,d20,d100) and # of rolls')

        return

    die = sys.argv[1]
    roll_count = sys.argv[2]

    roll(die, roll_count)

def roll(die, roll_count):
    limit = int(die.replace('d',''))

    for x in range(0, int(roll_count)):
        roll = secrets.randbelow(limit) + 1

        print(die + ': ' + str(roll))

if __name__ == "__main__":
    main()
