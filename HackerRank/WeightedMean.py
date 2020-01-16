# Submission
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
array1 = input().split()
array2 = input().split()

def weightedMean(arr1, arr2):
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator = numerator + float(arr1[i]) * float(arr2[i])
        denominator = denominator + float(arr2[i])
    weighted_mean = numerator/denominator
    print('{a:.1f}'.format(a = weighted_mean))

weightedMean(array1, array2)

###############################
# # Local
# f = open("data/input.txt", "r")
# n = int(f.readline())
# array1 = f.readline().split()
# array2 = f.readline().split()
# f.close()
#
# def weightedMean(arr1, arr2):
#     numerator = 0
#     denominator = 0
#     for i in range(n):
#         numerator = numerator + float(arr1[i]) * float(arr2[i])
#         denominator = denominator + float(arr2[i])
#     weighted_mean = numerator/denominator
#     print('{a:.1f}'.format(a = weighted_mean))
#
# weightedMean(array1, array2)
