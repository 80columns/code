# inspired by https://www.youtube.com/watch?v=XKu_SEDAykw

import random

def main():
    sum = random.randint(1, 100)
    numbers = []

    for x in range(0, 100):
        numbers.append(random.randint(1, sum))

    print(f'searching {numbers} for a pair that adds to {sum}')

    FindSumPair(numbers, sum)

def FindSumPair(numbers, sum):
    differences = set()
    success = False

    for x in numbers:
        if x in differences:
            print(f'found {sum - x} + {x} = {sum}')

            success = True
            break
        else:
            differences.add(sum - x)

    return success


if __name__ == "__main__":
    main()