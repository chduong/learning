###################################
# Build 2 stacks, 1 to keep track of the max value and 1 to keep track of actual values. Print from max value from max_stack.
N = int(input())
stack = []
max_stack = [0]

for _ in range(N):
    item = [int(x) for x in input().split()]

    if item[0] == 1:
        stack.append(item[1])
        max_stack.append(max(item[1], max_stack[-1]))

    elif item[0] == 2:
        if stack.pop() <= max_stack[-1]:
            max_stack.pop()

    elif item[0] == 3:
        print(max_stack[-1])

###################################
# max() is terribly slow, O(n**2), so bad solution, although short
# import sys
#
# N = int(input())
#
# stack = [0]
#
# for i in range(N):
#     item = [int(x) for x in input().split()]
#     if item[0] == 1:
#         stack.append(item[1])
#     elif item[0] == 2:
#         stack.pop()
#     elif item[0] == 3:
#         print(max(stack))

###################################
# # LOCAL
# import sys
#
# sys.stdin = open('data/input.txt', 'r')
#
# N = int(input())
# stack = []
# max_stack = [0]
#
# for _ in range(N):
#     item = [int(x) for x in input().split()]
#
#     if item[0] == 1:
#         stack.append(item[1])
#         max_stack.append(max(item[1], max_stack[-1]))
#
#     elif item[0] == 2:
#         if stack.pop() <= max_stack[-1]:
#             max_stack.pop()
#
#     elif item[0] == 3:
#         print(max_stack[-1])
#
# sys.stdin.close()