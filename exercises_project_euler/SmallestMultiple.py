# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Euclid's Algorithm:
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)
# where
# a mod b = a - b |a / b|

# If the arguments are both greater than zero then the algorithm can be written in more elementary terms as follows:
# gcd(a, a) = a
# gcd(a, b) = gcd(a - b, b), if a > b
# gcd(a, b) = gcd(a, b - a) , if b > a
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# definition from wikipedia: https://en.wikipedia.org/wiki/Least_common_multiple
# lcm (a, b) = |a * b| / gcd(a, b)
def lcm(a, b):
    return a * b / gcd(a, b)

def smallestMultiple(start, end):
    n = 1
    for i in range(start, end):
        n = lcm(n, i) # finds the lcm for a given (n, i) for i in range(start, end)
        # print(n) # check to visualize the lcm at each i in range.
    print(n)

smallestMultiple(1, 20)
# output: 232792560.0