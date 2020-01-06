# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */

# returns smallest multiple that is evenly divisible by all numbers from 1 - n
# returns -1 if multiple does not exist
def findSmallestMultiple(n):
    for i in range(n, factorial(n) + 1, n):
        if isMultiple(i, n):
            return i
    return -1

# checks every number between 1 and n to see if x is a multiple of every number
# returns True if x is found to be a multiple of every number, and False if x is
# found to not be a multiple of any number
def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

# returns the n factorial, or -1 if it does not exist
def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (findSmallestMultiple(10)) # 2520
print (findSmallestMultiple(20))


##################################
# FAST
#
# Solution to Project Euler problem 5
# Copyright (c) Project Nayuki. All rights reserved.
#
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
#

import fractions


# The smallest number n that is evenly divisible by every number in a set {k1, k2, ..., k_m}
# is also known as the lowest common multiple (LCM) of the set of numbers.
# The LCM of two natural numbers x and y is given by LCM(x, y) = x * y / GCD(x, y).
# When LCM is applied to a collection of numbers, it is commutative, associative, and idempotent.
# Hence LCM(k1, k2, ..., k_m) = LCM(...(LCM(LCM(k1, k2), k3)...), k_m).
def compute():
	ans = 1
	for i in range(1, 21):
		ans *= i // fractions.gcd(i, ans)
	return str(ans)


if __name__ == "__main__":
	print(compute())

##################################
# FAST 2

def gcd(x,y): #Euclid's Algorithm gcd(a, a) = a; gcd(a, b) = gcd(a - b, b), if a > b; gcd(a, b) = gcd(a, b-a) , if b > a
    return y and gcd(y, x % y) or x
def lcm(x,y): # definition from wikipedia: https://en.wikipedia.org/wiki/Least_common_multiple
    return x * y / gcd(x,y)

n = 1
for i in range(1, 20):
     n = lcm(n, i)
print(n)