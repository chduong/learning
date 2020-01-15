# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import collections

num_shoes = sys.stdin.readline() #read first line for number of shoes
shoes = collections.Counter(map(int, sys.stdin.readline().split())) #read second line for available shoe sizes, counts them, and stores in a dictionary of sizes and available shoes
num_customers = int(sys.stdin.readline()) #read third line for number of customers

income = 0 #starting income

for _ in range(num_customers): #calculating the
    size, price = map(int, sys.stdin.readline().split())
    if shoes[size] != 0:
        income += price
        shoes[size] -= 1
    # else:
    #     print('Nothing to Sell')

print(income)

# ##############################
# import collections
#
# numShoes = int(input())
# shoes = collections.Counter(map(int, input().split()))
# numCust = int(input())
#
# income = 0
#
# for i in range(numCust):
#     size, price = map(int, input().split())
#     if shoes[size]:
#         income += price
#         shoes[size] -= 1
#
# print(income)