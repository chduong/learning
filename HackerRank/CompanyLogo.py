if __name__ == '__main__':
    s = input()

d = {}

for letter in s:
    if letter in d:
        d[letter] = d[letter] + 1
    else:
        d[letter] =  1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for l, c in list(d)[:3]:
    print('{l} {c}'.format(l=l, c=c))

###################################
# Elegant (from Boki)
# from collections import Counter, OrderedDict
#
# class OrderedCounter(Counter, OrderedDict):
#     pass
# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

###################################
# Data Incubator Solution
# from collections import defaultdict
#
# s = input()
# d = defaultdict(int)
# for c in s:
#     d[c] += 1
# counts = sorted(d.items(), key=lambda x: (-x[1], x[0]))
#
# for c, n in counts[:3]:
#     print('{c} {n}'.format(c=c, n=n))

###################################
# Compartmentalization with functions
# from collections import defaultdict
#
# def count_letters(s):
#     d = defaultdict(int)
#     for c in s:
#         d[c] += 1
#     return d
#
# def get_top_n(d, n=3):
#     return sorted(d.items(), key=lambda x: (-x[1], x[0]))[:n]
#
# def print_counts(counts):
#     for c, n in counts:
#         print('{c} {n}'.format(c=c, n=n))
#
# s = input()
# print_counts(get_top_n(count_letters(s)))

###################################
# from collections import defaultdict
#
# def count_letters(s):
#     d = defaultdict(int)
#     for c in s:
#         d[c] += 1
#     return d
#
# def get_top_n(d, n=3):
#     return sorted(d.items(), key=lambda x: (-x[1], x[0]))[:n]
#
# def print_counts(counts):
#     for c, n in counts:
#         print('{c} {n}'.format(c=c, n=n))
#
# if __name__ == '__main__':
#     s = input()
#     print_counts(get_top_n(count_letters(s)))