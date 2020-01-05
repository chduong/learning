# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
# Brute Force Method

def largestPrimeFactor(n):
    prime_factor = 1
    i = 2

    while i <= n / i: # iterates all numbers until i <= n / i
        if n % i == 0: # if there is no modulus for n / i, then i is a prime factor
            prime_factor = i # produces the prime_factors
            n = n / i # slowly factorizes n by i to smaller numbers until it is fully broken down into its prime factors
        else:
            i += 1 # if the first condition is not meant, there is no prime factor i, so +1 is added to i until it can be factored by i+1

    if prime_factor < n: # selects the largest prime factor, either prime_factor = i (smallest value going up), or n (largest value going down)
        prime_factor = n

    return prime_factor

print(largestPrimeFactor(600851475143))
