"""
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
"""

def climbSteps(n, cache):
    # climb 1, 2, or 3 steps at a time
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n not in cache:
        oneStep = cache[n - 1] if n - 1 in cache \
                               else climbSteps(n - 1, cache)
        twoSteps = cache[n - 2] if n - 2 in cache \
                                else climbSteps(n - 2, cache)
        threeSteps = cache[n - 3] if n - 3 in cache \
                                  else climbSteps(n - 3, cache)

        cache[n] = oneStep + twoSteps + threeSteps
    
    return cache[n]

def stepPerms(n):
    return climbSteps(n, {}) % 10000000007

def main():
    print(stepPerms(5))
    print(stepPerms(1))
    print(stepPerms(3))
    print(stepPerms(7))

if __name__ == "__main__":
    main()