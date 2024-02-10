#!/usr/bin/python

# https://www.hackerrank.com/challenges/making-candies/problem

def minimumPasses(m: int, w: int, p: int, n: int):
    candies = 0
    passes = 0
    minimum_passes = -1

    while True:
        # calculate how many candies can be made with the current machine-worker numbers
        new_candies = m * w

        # calculate how many passes need to be made before we can spend candies
        # to purchase a machine or hire a worker on the next pass
        if candies + new_candies < p:
            candies_until_spend = p - candies
            passes_until_spend, candies_remaining = divmod(candies_until_spend, new_candies)
            passes_until_spend -= 0 if candies_remaining > 0 else 1
            passes += passes_until_spend
            candies += new_candies * passes_until_spend

        if passes == minimum_passes:
            break

        # calculate how many passes it would take to get to the target if no machines
        # are purchased and no workers are hired on the remaining passes
        candies_until_target = n - candies
        passes_until_target, remainder = divmod(candies_until_target, new_candies)
        passes_until_target += 1 if remainder > 0 else 0
        passes_to_n = passes + passes_until_target

        if passes_to_n < minimum_passes or minimum_passes == -1:
            minimum_passes = passes_to_n
        elif passes_to_n > minimum_passes:
            break

        candies_to_spend = candies + new_candies
        passes += 1
        new_production_units, candies = divmod(candies_to_spend, p)

        # produce the best combination of spending candies on machines and workers
        # units are added to m and w so that they are as close in value as possible,
        # as this will generate the highest product when multiplying them
        if w < m:
            temp_w = w
            w += new_production_units if (m - w) > new_production_units else (m - w)
            new_production_units -= (m - temp_w)
        elif m < w:
            temp_m = m
            m += new_production_units if (w - m) > new_production_units else (w - m)
            new_production_units -= (w - temp_m)

        if new_production_units > 0:
            half_new_production_units, units_remainder = divmod(new_production_units, 2)
            m += half_new_production_units
            w += half_new_production_units

            m += 1 if units_remainder == 1 else 0

    return minimum_passes


def main():
    '''
    m = number of machines which make candies
    w = number of workers
    p = cost to hire a new worker or purchase a new machine, in candies
    n = number of candies which need to be produced
    '''

    print(minimumPasses(m=3, w=1, p=2, n=12)) # output should be 3
    print(minimumPasses(m=1, w=2, p=1, n=60)) # output should be 4

if __name__ == "__main__":
    main()
