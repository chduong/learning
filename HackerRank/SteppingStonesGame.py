import os
import sys
import math

# Complete the solve function below.

# From wikipedia: https://en.wikipedia.org/wiki/Triangular_number
def triangular_num(x):
    # x is an integer if 8 * x + 1 is a squared number
    if math.sqrt(8 * x + 1) % 1 == 0:
        # Definition of triangular numbers
        n = (math.sqrt(8 * x + 1) - 1) / 2
        return int(n)
    return -1

# Print results
def solve(n):
    num = triangular_num(n)
    if triangular_num(n) > -1:
        return 'Go On Bob ' + str(num)
    else:
        return 'Better Luck Next Time'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

####### LOCAL
# import sys
# import math
#
# def triangular_num(x):
#     # x is an integer if 8 * x + 1 is a squared number
#     if math.sqrt(8 * x + 1) % 1 == 0:
#         # Definition of triangular numbers
#         n = (math.sqrt(8 * x + 1) - 1) / 2
#         return int(n)
#     return -1
#
# # Print results
# def solve(n):
#     num = triangular_num(n)
#     if triangular_num(n) > -1:
#         return 'Go On Bob ' + str(num)
#     else:
#         return 'Better Luck Next Time'
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     t = int(sys.stdin.readline())
#
#     for t_itr in range(t):
#         n = int(sys.stdin.readline())
#
#         result = solve(n)
#         print(result)