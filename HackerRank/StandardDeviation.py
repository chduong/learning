import math

n = int(input())
array1 = [int(x) for x in input().split()]

def mean(arr1):
    sum = 0
    for i in array1:
        sum = sum + i
    mean_val = sum / n
    return mean_val

# print(mean(array1))

def standardDeviation(arr1):
    u = mean(arr1)
    # print(u)
    sigma_numerator = 0
    for i in range(n):
        sigma_numerator = sigma_numerator + (arr1[i] - u)**2
    sigma = math.sqrt(sigma_numerator / n)
    print(round(sigma, 1))

standardDeviation(array1)

#############################################
# # Local
# import math
#
# f = open('data/input.txt', 'r')
#
# n = int(f.readline())
# array1 = [int(x) for x in f.readline().split()]
#
# def mean(arr1):
#     sum = 0
#     for i in array1:
#         sum = sum + i
#     mean_val = sum / n
#     return mean_val
#
# # print(mean(array1))
#
# def standardDeviation(arr1):
#     u = mean(arr1)
#     # print(u)
#     sigma_numerator = 0
#     for i in range(n):
#         sigma_numerator = sigma_numerator + (arr1[i] - u)**2
#     sigma = math.sqrt(sigma_numerator / n)
#     print(round(sigma, 1))
#
# standardDeviation(array1)