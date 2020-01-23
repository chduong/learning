# Complexity ~ O(2n)
import os

# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr) == 1:
        return 'YES'
    else:
        left_sum = 0
        right_sum = sum(arr)
        for index in range(len(arr)):
            current = arr[index]
            right_sum -= current
            if left_sum == right_sum:
                return 'YES'
            left_sum += current
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

# #######################
# # Alternatives O(2n)
# def balancedSums(arr):
#     sum1 = 0
#     sum2 = sum(arr)
#
#     for item in arr:
#         sum2 -= item
#         if sum1 == sum2:
#             return "YES"
#         sum1 += item
#     return "NO"

# #######################
# LOCAL
# import sys
#
# # Complete the balancedSums function below.
# def balancedSums(arr):
#     if len(arr) == 1:
#         return 'YES'
#     else:
#         left_sum = 0
#         right_sum = sum(arr)
#         for index in range(len(arr)):
#             current = arr[index]
#             right_sum -= current
#             if left_sum == right_sum:
#                 return 'YES'
#             left_sum += current
#         return 'NO'
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     T = int(input().strip())
#
#     for T_itr in range(T):
#         n = int(input().strip())
#
#         arr = list(map(int, input().rstrip().split()))
#
#         result = balancedSums(arr)
#
#         print(result)
#
#         # fptr.write(result + '\n')
#
#     sys.stdin.close()