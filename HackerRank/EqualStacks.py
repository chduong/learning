import os
import sys
from functools import reduce
from itertools import accumulate
# import operator # if you want to change operator from accumulate's standard (add)

# Best approach uses sets and reduce to find common elements in list of lists
def equalStacks(h1, h2, h3):
    stacks = [h1, h2, h3]
    accumulates = [set(accumulate([0] + stack[::-1])) for stack in stacks]
    match = reduce(set.intersection, accumulates)
    return max(match)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

#################################
# # Faster, from HackerRank
# def getConvertedStack(stack):
#     outStack = []
#     for i in range(0,len(stack)):
#         if (i == 0):
#             acc = 0
#             for j in range(i, len(stack)):
#                 acc +=stack[j]
#             outStack.append(acc)
#         else:
#             acc = acc -stack[i-1]
#             outStack.append(acc)
#
#     return outStack

#################################
# # Brute Force, too slow, from HackerRank
# n1,n2,n3 = raw_input().strip().split(' ')
# n1,n2,n3 = [int(n1),int(n2),int(n3)]
# h1 = map(int,raw_input().strip().split(' '))[::-1]
# h2 = map(int,raw_input().strip().split(' '))[::-1]
# h3 = map(int,raw_input().strip().split(' '))[::-1]
# h1 = [sum(h1[:i+1]) for i in range(len(h1))]
# h2 = [sum(h2[:i+1]) for i in range(len(h2))]
# h3 = [sum(h3[:i+1]) for i in range(len(h3))]
#
# while h1[-1] != h2[-1] or h2[-1] != h3[-1]:
#     if h1[-1] > h2[-1] or h1[-1] > h3[-1]:
#         h1.pop()
#     elif h2[-1] > h1[-1] or h2[-1] > h3[-1]:
#         h2.pop()
#     elif h3[-1] > h2[-1] or h3[-1] > h1[-1]:
#         h3.pop()
# print h1[-1]

#################################
# #LOCAL
# import sys
# from functools import reduce
# from itertools import accumulate
# # import operator # if you want to change operator from accumulate's standard (add)
#
# # Complete the equalStacks function below.
# def equalStacks(h1, h2, h3):
#     stacks = [h1, h2, h3]
#     accumulates = [set(accumulate([0] + stack[::-1])) for stack in stacks]
#     match = reduce(set.intersection, accumulates)
#     return max(match)
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     n1N2N3 = input().split()
#
#     n1 = int(n1N2N3[0])
#
#     n2 = int(n1N2N3[1])
#
#     n3 = int(n1N2N3[2])
#
#     h1 = list(map(int, input().rstrip().split()))
#
#     h2 = list(map(int, input().rstrip().split()))
#
#     h3 = list(map(int, input().rstrip().split()))
#
#     result = equalStacks(h1, h2, h3)
#
#     # fptr.write(str(result) + '\n')
#
#     sys.stdin.close()

