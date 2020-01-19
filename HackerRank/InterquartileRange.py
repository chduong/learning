## NOTE: Not the best definition of interquartile, works best for continuous cases, but not widely discrete cases

import statistics as st
n = int(input())
data = [int(x) for x in input().split()]
freq = [int(y) for y in input().split()]

S = []
for i in range(n):
    S += [data[i]] * freq[i]
S.sort()

mid = sum(freq) // 2

if n % 2 == 0:
    q1 = st.median(S[:mid])
    q3 = st.median(S[mid:])
else:
    q1 = st.median(S[:mid])
    q3 = st.median(S[mid + 1:])

print('%.1f' % (q3-q1))


# ###################################
# # Local
# f = open('data/input.txt', 'r')
#
# import statistics as st
# n = int(f.readline())
# data = [int(x) for x in f.readline().split()]
# freq = [int(y) for y in f.readline().split()]
#
# S = []
# for i in range(n):
#     S += [data[i]] * freq[i]
# S.sort()
#
# mid = sum(freq) // 2
#
# if n % 2 == 0:
#     q1 = st.median(S[:mid])
#     q3 = st.median(S[mid:])
# else:
#     q1 = st.median(S[:mid])
#     q3 = st.median(S[mid + 1:])
#
#print('%.1f' % (q3-q1))