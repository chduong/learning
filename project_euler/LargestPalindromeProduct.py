# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# [ : :-1] = slices list in reverse order.
# [ : :2] = slices list in increments of 2.
# [start:end:steps] = format

def largestPalindrome(i, j):
    palindrome = 0
    for x in range(i, j, 1):
        for y in range(x, j, 1): # Cuts the matrix of the y for loop down, instead of iterating between i and j, you can iterate between x and j since the combination of x * y is also the same as y * x
            temp = x * y
            if temp > palindrome:
                if str(x * y) == str(x * y)[::-1]:
                    palindrome = x * y
    return str(palindrome)

print(largestPalindrome(100, 999))
