from itertools import combinations

n = input()
strings = [str(x) for x in input().split()]
k = int(input())

combinations = list(combinations(strings, k))
contains_a = filter(lambda string: 'a' in string, combinations)
contains_a_list = list(contains_a)

print('{0:.3}'.format(len(contains_a_list)/len(combinations)))

#######################
# # LOCAL, Slow, O(n!)
# f = open('data/input.txt', 'r')
#
# from itertools import combinations
#
# n = f.readline()
# strings = [str(x) for x in f.readline().split()]
# k = int(f.readline())
#
# combinations = list(combinations(strings, k))
# contains_a = filter(lambda string: 'a' in string, combinations)
# contains_a_list = list(contains_a)
#
# print(combinations)
# print(contains_a_list)
# print('%.3f' % (len(contains_a_list)/len(combinations)))

#######################
# From GeeksforGeeks to understand itertools
# # function that filters vowels
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
#
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print('The filtered letters are:')
# for s in filtered:
#     print(s)

#######################
# Application with lambda functions:
# # a list contains both even and odd numbers.
# seq = [0, 1, 2, 3, 5, 8, 13]
#
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2, seq)
# print(list(result))
#
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))