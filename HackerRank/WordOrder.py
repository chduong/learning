import collections

n = int(input())

dict = collections.OrderedDict()

for i in range(n):
    word = input()
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(len(dict))

for key, value in dict.items():
    print(value, end=' ')

# ##################
#
# import collections
#
# n = int(input())
#
# dict = collections.OrderedDict()
#
# for i in range(n):
#     word = input()
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
#
# print(len(dict))
#
# value_list = []
#
# for key, value in dict.items():
#     value_list.append(value)
#
# print(*value_list, sep=' ')
# ####################
#
# import sys
# _ = sys.stdin.readline()
# words = sys.stdin.read().split()
#
# d = dict()
# order = 0
# for word in words:
#     if word in d:
#         d[word] = (d[word][0], d[word][1] + 1)
#     else:
#         d[word] = (order, 1)
#         order += 1
#
# print(len(d))
# ordered_counts = sorted(d.values())
# for order, count in ordered_counts:
#     print(count, end=' ')
#
# ####################
# # FAILED ATTEMPTS AND NOTES BELOW HERE
# ####################
# #
# # print(list[0])
# # from collections import OrderedDict
# #
# # import pandas as pd
# #
# # df = pd.DataFrame({'words':list[:]})
# #
# # df = df['words'].nunique()
# #
# # print(df)
#
# ####################
#
# # for _ in words: #use _ when the code is not used or needed for other parts of code, improves readability
# #     print(words[0])
# # dictionary complexity is order n (very fast)
# # assign to _ is not needed.
#
# # my_list = [(1, 9), (3, 3), (2, 3), (0, -1), (4, 5), (0, -2)]
# # sorted(my_list, key = lambda x: (x[-1], x[0]))