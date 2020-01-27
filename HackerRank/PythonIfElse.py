#!/bin/python3

import sys

if __name__ == '__main__':

    sys.stdin = open('data/input.txt', 'r')
    n = int(input().strip())
    sys.stdin.close()

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and n >= 2 and n <= 5:
    print('Not Weird')
elif n % 2 == 0 and n >= 6 and n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')