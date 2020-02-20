#!/bin/python3

import os

# k = number of friends
# c = cost of flowers
def getMinimumCost(k, c):
    c.sort(reverse = True)
    total = 0

    for flower_index, cost in enumerate(c):
        total += cost * (1 + (flower_index // k))

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

####### LOCAL
import sys

# Complete the getMinimumCost function below.
# k = number of friends
# c = cost of flowers
def getMinimumCost(k, c):
    c.sort(reverse = True)
    total = 0

    for flower_index, cost in enumerate(c):
        total += cost * (1 + (flower_index // k))
        # Floor division of the flower_index by the number of friends keeps track of when each friend has purchased a flower before the florist increases the price.

    return total

if __name__ == '__main__':
    sys.stdin = open('data/input.txt', 'r')

    nk = sys.stdin.readline().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, sys.stdin.readline().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)
    # print(list(enumerate(c)))