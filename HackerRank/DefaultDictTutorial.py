from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)
b = []

for i in range(n):
    a[input()].append(i + 1) # 1-indexed

for i in range(m):
    b = b + [input()]

for word in b:
    if word in a:
        print(" ".join(map(str, a[word]))) #prints index of word in group a
    else:
        print(-1) # not in dictionary list

##########################################

from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1)

for i in range(0,m):
    list1=list1+[raw_input()]

for i in list1:
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1