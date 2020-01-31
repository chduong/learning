#!/bin/python3
import os

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = sum([1 if x[0] > x[1] else 0 for x in zip(a, b)])
    b_score = sum([1 if x[1] > x[0] else 0 for x in zip(a, b)])
    return (a_score, b_score)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

##########
# # LOCAL
#
# import sys
#
# # Complete the compareTriplets function below.
# def compareTriplets(a, b):
#     a_score = sum([1 if x[0] > x[1] else 0 for x in zip(a, b)])
#     b_score = sum([1 if x[1] > x[0] else 0 for x in zip(a, b)])
#     return (a_score, b_score)
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
#     result = compareTriplets(a, b)
#
#     print(result)
#
#     sys.stdin.close()