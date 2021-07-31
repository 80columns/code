"""
 There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
 Given N, write a function that returns the number of unique ways you can climb
 the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time. Generalize your function
to take in X. 
"""

# height = N, steps = X
def climb_staircase_recursive(height, steps, record):
    if height not in record:
        record[height] = 0

        for step in steps:
            if height - step == 0:
                record[height] += 1
            elif height - step > 0:
                record[height] += \
                    climb_staircase_recursive(height - step, steps, record)

    return record[height]

def main():
    print(climb_staircase_recursive(4, {1, 2}, {}))

if __name__ == "__main__":
    main()