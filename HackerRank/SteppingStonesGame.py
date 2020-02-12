import os
import sys
from decimal import *

# Set decimal precision (for working with large numbers, 50 characters is arbitrary).
# If this precision is too large, you will fail some test cases due to timeout.
getcontext().prec = 50

def triangular_num(x):
    # x is an integer if 8 * x + 1 is a squared number, thus the square root's modulus should not have a remainder
    if Decimal(8 * x + 1).sqrt() % Decimal(1) == 0:
        # Definition of triangular numbers (from positive component of quadratic equation)
        n = Decimal((8 * x + 1) - 1).sqrt() / Decimal(2)
        return int(n)
    return -1


# Print results
def solve(n):
    num = triangular_num(n)

    if num > -1:
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
# from decimal import *
#
# # Set decimal precision (for working with large numbers, 50 characters is arbitrary).
# # If this precision is too large, you will fail some test cases due to timeout.
# getcontext().prec = 50
#
# def triangular_num(x):
#     # x is an integer if 8 * x + 1 is a squared number, thus the square root's modulus should not have a remainder
#     if Decimal(8 * x + 1).sqrt() % Decimal(1) == 0:
#         # Definition of triangular numbers (from positive component of quadratic equation)
#         n = Decimal((8 * x + 1) - 1).sqrt() / Decimal(2)
#         return int(n)
#     return -1
#
#
# # Print results
# def solve(n):
#     num = triangular_num(n)
#
#     if num > -1:
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

####### SIDE NOTE: To find the n_th triangular number (in this case, x = 10**499):
# x = Decimal(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

# # Formula:
# num = Decimal(x * (x + 1)) / Decimal(2)