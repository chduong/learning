#!/bin/python3
import os
import sys

# Construct all substrings of a string
def substrings(string, size):
    s1 = string[:size]
    size1 = len(s1) + 1
    s2 = string[size:]
    size2 = len(s2) + 1
    N = [[0 for j in range(size2)] for i in range(size1)]

    for i in range(1, size1):
        for j in range(1, size2):
            # Case when s1[i] == s2[j]
            if s1[i - 1] == s2[j - 1]:
                N[i][j] = N[i - 1][j] + N[i][j - 1] + 1
            else:
                # Case when s1[i] != s2[j]
                N[i][j] = N[i - 1][j] + N[i][j - 1] - N[i - 1][j - 1]

    # The number of matching pairs for each size.
    return N[-1][-1] - N[-2][-1]

# Counts the square sequences for a string (s) and iterating through the size of the string (size), divided by a number defined by the problem.
def squareSubsequences(s):
    count = sum(substrings(s, size) for size in range(1, len(s)))
    number = 1000000007
    return count % number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = squareSubsequences(s)

        fptr.write(str(result) + '\n')

    fptr.close()

####### LOCAL
# import os
# import sys
#
# # Construct all substrings of a string
# def substrings(string, size):
#     s1 = string[ :size]
#     size1 = len(s1) + 1
#     s2 = string[size: ]
#     size2 = len(s2) + 1
#     N = [[0 for j in range(size2)] for i in range(size1)]
#
#     for i in range(1, size1):
#         for j in range(1, size2):
#             # Case when s1[i] == s2[j]
#             if s1[i - 1] == s2[j - 1]:
#                 N[i][j] = N[i-1][j] + N[i][j - 1] + 1
#             else:
#             # Case when s1[i] != s2[j]
#                 N[i][j] = N[i - 1][j] + N[i][j - 1] - N[i - 1][j - 1]
#
#     # The number of matching pairs for each size.
#     return N[-1][-1] - N[-2][-1]
#
# # Counts the square sequences for a string (s) and iterating through the size of the string (size), divided by a number defined by the problem.
# def squareSubsequences(s):
#     count = sum(substrings(s, size) for size in range(1, len(s)))
#     number = 1000000007
#     return count % number
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     t = int(sys.stdin.readline())
#
#     for t_itr in range(t):
#         s = sys.stdin.readline()
#
#         result = squareSubsequences(s)
#
#         print(result)