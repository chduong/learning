import numpy as np
from scipy import stats

n = int(input())

data = list(map(int, input().split()))

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)

print(mean)
print(median)
print(int((mode)[0]))

####################################

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

####################################

import numpy as np
from scipy import stats

# n = int(input())
#
# a = []
# for i in range(n):
#     a = a.extend(input())
#
# print(a)
#
# data = np.array(input())
#
# mean = np.mean(data)
#
# median = np.median(data)
#
# mode = stats.mode(data)
#
# print(mean)
# print(median)
# print(mode)

#####################

