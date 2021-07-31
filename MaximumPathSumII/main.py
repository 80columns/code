"""
https://projecteuler.net/problem=67

Input:
A triangle of integers with 100 rows

Output:
The total sum of integers in the maximum path from the top to the bottom


Sample input:
   3
  7 4
 2 4 6
8 5 9 3

Sample output:
23

i.e., 3 + 7 + 4 + 9 = 23
"""

# bottom-up approach
def get_max_path_iterative(triangle):
    last_inner_row = len(triangle) - 2

    for x in range(last_inner_row, -1, -1):
        for y in range(0, len(triangle[x])):
            left_element = triangle[x + 1][y]
            right_element = triangle[x + 1][y + 1]

            triangle[x][y] += left_element if left_element > right_element \
                                         else right_element

        triangle.pop()

    return triangle[0][0]

# top-down approach
def get_max_path_recursive(triangle, x, y, max_paths):
    # x is row, y is column
    if (x, y) not in max_paths:
        if x == len(triangle) - 2:
            left_element = triangle[x + 1][y]
            right_element = triangle[x + 1][y + 1]

            max_child_element = left_element if left_element > right_element \
                                           else right_element

            max_paths[(x, y)] = triangle[x][y] + max_child_element
        else:
            max_left_path = get_max_path_recursive(triangle, \
                                                   x + 1, \
                                                   y, \
                                                   max_paths)
            max_right_path = get_max_path_recursive(triangle, \
                                                    x + 1, \
                                                    y + 1, \
                                                    max_paths)

            max_child_path = max_left_path if max_left_path > max_right_path \
                                         else max_right_path

            max_paths[(x, y)] = triangle[x][y] + max_child_path

    return max_paths[(x, y)]

def main():
    triangle = []

    with open("p067_triangle.txt") as input_file:
        input_text = input_file.readlines()

    for line in input_text:
        triangle.append([int(x) for x in line.replace("\n", "").split(" ")])

    print(get_max_path_recursive(triangle, 0, 0, {}))
    print(get_max_path_iterative(triangle))

if __name__ == "__main__":
    main()