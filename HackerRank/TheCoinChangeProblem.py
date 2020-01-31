#!/bin/python3
# Python 3.7

import os

count_dict = {}

def getWays(n, c):
    if len(c) == 0:
        return 0
    if n < 0:
        return 0
    if n == 0:
        return 1

    key = (n, tuple(c))
    if key not in count_dict:
        count_dict[key] = getWays(n - c[0], c) + getWays(n, c[1:])
    return count_dict[key]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()

########
# # LOCAL
#
# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# count_dict = {}
#
# def getWays(n, c):
#     if len(c) == 0:
#         return 0
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#
#     key = (n, tuple(c))
#
#     if key not in count_dict:
#         count_dict[key] = getWays(n - c[0], c) + getWays(n, c[1:])
#         print(count_dict)
#     return count_dict[key]
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     first_multiple_input = input().rstrip().split()
#
#     n = int(first_multiple_input[0])
#
#     m = int(first_multiple_input[1])
#
#     c = list(map(int, input().rstrip().split()))
#
#     # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#
#     ways = getWays(n, c)
#
#     print(str(ways) + '\n')
#
#     sys.stdin.close()
