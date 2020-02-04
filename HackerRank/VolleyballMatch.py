# import math
#
# def combinations_available(n, k):
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     import sys
#     a = int(sys.stdin.readline())
#     b = int(sys.stdin.readline())
#     print(combination_of_games(a, b) % 1000000007)

#######
# LOCAL
import math

def combinations_available(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def combination_of_games(a, b):
    # Consider edge cases (4/5)
    if a < b:
        a, b = b, a
    if a < 25:
        return 0
    if a == 25 and b > 23 and b < 27:
        return 0
    if a > 25 and a - b != 2:
        return 0

    # Base case
    if a == 25:
        return combinations_available(24 + b, 24)

    # Last edge case a,b == 24, 2 possibilities for every 2 points above 24 points and b (the limiter for the combinations above 24) is always the smaller of the 2 values since we swap the orders with the if a < b statement above.
    return combinations_available(48, 24) * 2**(b-24)

if __name__ == '__main__':
    import sys
    sys.stdin = open('data/input.txt', 'r')
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(combination_of_games(a, b) % 1000000007)
    sys.stdin.close()