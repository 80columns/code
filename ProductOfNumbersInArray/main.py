"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1] the expected output would be
[2, 3, 6].
"""

# Follow-up: what if you can't use division?
def GenerateArrayProductWithoutDivision1(arr):
    product_stack = []
    output_arr = [0 for x in range(len(arr))]

    for x in range(0, len(arr) - 1):
        for y in range(0, len(product_stack)):
            product_stack[y] *= arr[x]

        product_stack.append(arr[x])

    # the last value in the output array is the product of indexes 0*1*...*n-1
    output_arr[len(arr) - 1] = product_stack.pop(0)

    for y in range(0, len(product_stack)):
        product_stack[y] *= arr[len(arr) - 1]

    product_stack.append(arr[len(arr) - 1])

    for x in range(0, len(arr) - 1):
        output_arr[x] = product_stack.pop(0)

        for y in range(0, len(product_stack)):
            product_stack[y] *= arr[x]

    return output_arr

def GenerateArrayProductWithoutDivision2(arr):
    product = 1

    for x in arr:
        product *= x

    for i in range(0, len(arr)):
        temp_product = product
        result = 0

        while temp_product > 0:
            temp_product -= arr[i]
            result += 1

        arr[i] = result

    return arr

def GenerateArrayProduct(arr):
    product = 1

    for x in arr:
        product *= x

    for i in range(0, len(arr)):
        arr[i] = product // arr[i]

    return arr

def main():
    print(GenerateArrayProduct([10, 2, 3, 4, 5]))
    print(GenerateArrayProductWithoutDivision1([10, 2, 3, 4, 5]))
    print(GenerateArrayProductWithoutDivision2([10, 2, 3, 4, 5]))
    
    print(GenerateArrayProduct([3, 2, 1]))
    print(GenerateArrayProductWithoutDivision1([3, 2, 1]))
    print(GenerateArrayProductWithoutDivision2([3, 2, 1]))

if __name__ == "__main__":
    main()