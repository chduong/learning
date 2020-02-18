#!/bin/python3

import os

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)

    i = findPivot(w)
    if i <= 0:
        return 'no answer'

    j = findSuccessorToPivot(w, i)
    if j <= 0:
        return 'no answer'

    # Replacing the pivot and return the next lexicographical order string.
    w[i - 1], w[j] = w[j], w[i - 1]
    next_permutation = w[ :i] + w[ :i-1: -1]
    return ''.join(next_permutation)

# Find the non-increasing suffix
def findPivot(w):
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1
    return i

# Find the next element to replace the pivot
def findSuccessorToPivot(w, i):
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


####### LOCAL
# import sys
#
# # Complete the biggerIsGreater function below.
# def biggerIsGreater(w):
#     w = list(w)
#
#     i = findPivot(w)
#     if i <= 0:
#         return 'no answer'
#
#     j = findSuccessorToPivot(w, i)
#     if j <= 0:
#         return 'no answer'
#
#     # Replacing the pivot and return the next lexicographical order string.
#     w[i - 1], w[j] = w[j], w[i - 1]
#     next_permutation = w[ :i] + w[ :i-1: -1]
#     return ''.join(next_permutation)
#
# # Find the non-increasing suffix
# def findPivot(w):
#     i = len(w) - 1
#     while i > 0 and w[i - 1] >= w[i]:
#         i -= 1
#     return i
#
# # Find the next element to replace the pivot
# def findSuccessorToPivot(w, i):
#     j = len(w) - 1
#     while w[j] <= w[i - 1]:
#         j -= 1
#     return j
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     T = int(sys.stdin.readline())
#
#     for T_itr in range(T):
#         w = str(sys.stdin.readline().rstrip())
#
#         result = biggerIsGreater(w)
#
#         print(result)
