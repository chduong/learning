import statistics
n = int(input())
mid = n // 2
array1 = [int(x) for x in input().split()]
array1.sort()

if n % 2 == 0:
    q1 = statistics.median(array1[ :mid])
    q2 = statistics.median(array1)
    q3 = statistics.median(array1[mid: ])
    print('%.0f' % q1)
    print('%.0f' % q2)
    print('%.0f' % q3)
else:
    q1 = statistics.median(array1[ :mid])
    q2 = statistics.median(array1)
    q3 = statistics.median(array1[mid+1: ])
    print('%.0f' % q1)
    print('%.0f' % q2)
    print('%.0f' % q3)

####################################
# # Local
# f = open('data/input.txt', 'r')
#
# import statistics
# n = int(f.readline())
# mid = n // 2
# array1 = [int(x) for x in f.read().split()]
# array1.sort()
#
# if n % 2 == 0:
#     q1 = statistics.median(array1[ :mid])
#     q2 = statistics.median(array1)
#     q3 = statistics.median(array1[mid: ])
#     print('%.0f' % q1)
#     print('%.0f' % q2)
#     print('%.0f' % q3)
# else:
#     q1 = statistics.median(array1[ :mid])
#     q2 = statistics.median(array1)
#     q3 = statistics.median(array1[mid+1: ])
#     print('%.0f' % q1)
#     print('%.0f' % q2)
#     print('%.0f' % q3)