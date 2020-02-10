from fractions import Fraction

# Compute the valid pairs
def num_valid_pairs(arr, k):
    total = 0
    window = 0

    for i in range(len(arr)):
        if arr[i]:
            total += window
            window += 1
        if i >= k and arr[i-k]:
            window -= 1

    total *= 2

    total += sum(arr)

    return total

# Print in proper format
def print_fraction(arr, k):
    num = num_valid_pairs(arr, k)

    den = len(arr)**2

    if num == den:
        print("1/1")
    elif num:
        print(Fraction(num, den))
    else:
        print("0/1")

if __name__ == '__main__':
    import sys

    tests = int(sys.stdin.readline())
    for i in range(tests):
        N, K = map(int, sys.stdin.readline().split())
        arr_s = list(map(int, sys.stdin.readline().strip()))
        print_fraction(arr_s, K)

####### LOCAL, TOO SLOW
# import os
# import sys
# from fractions import Fraction
#
# # Complete the solve function below.
# def solve(n, k, s):
#     s = str(s)
#     n = len(s)
#     total_combos = []
#     valid_combos = []
#
#     for i in range(0, n):
#         for j in range(0, n):
#             total_combos.append((i, j))
#             if abs(i-j)<=k:
#                 if s[i]=='1' and s[j]=='1':
#                     valid_combos.append((i, j))
#     if len(valid_combos)==0:
#         return str(0)+'/'+str(1)
#     else:
#         return str(len(valid_combos)) + '/' + str(len(total_combos))
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     trials = int(sys.stdin.readline())
#
#     for trial_itr in range(trials):
#         n, k = map(int, sys.stdin.readline().split())
#
#         s = int(sys.stdin.readline())
#
#         result = solve(n, k, s)
#         print(result)

####### LOCAL (FASTER)
# from fractions import Fraction
#
# # Compute the valid pairs
# def num_valid_pairs(arr, k):
#     total = 0
#     window = 0
#
#     for i in range(len(arr)):
#         if arr[i]:
#             total += window
#             window += 1
#             print(window)
#         if i >= k and arr[i-k]: # Prevents double counting
#             window -= 1
#             print(window)
#
#     total *= 2         # Counts reverse ordered pairs, [0, 1] and [1, 0]
#
#     total += sum(arr)  # Counts valid selections if the index value is selected for i and j.
#
#     return total
#
# # Print in proper format
# def print_fraction(arr, k):
#     num = num_valid_pairs(arr, k)
#
#     den = len(arr)**2 # total combinations is nCr = n! / r! (n-r)!, where n = number of items (length of string S) and r = number of items being chosen (2, since each item in string is 0 or 1). In this sample case, 4! / 2! (4-2)! = 16.
#
#     if num == den:
#         print("1/1")
#     elif num:
#         print(Fraction(num, den))
#     else:
#         print("0/1")
#
# if __name__ == '__main__':
#     import sys
#     sys.stdin = open('data/input.txt', 'r')
#     tests = int(sys.stdin.readline())
#     for i in range(tests):
#         N, K = map(int, sys.stdin.readline().split())
#         arr_s = list(map(int, sys.stdin.readline().strip()))
#         print_fraction(arr_s, K)

