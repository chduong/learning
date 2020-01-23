############################
# # Using Stacks:
import os

pair = {')':'(','}':'{',']':'['}

def isBalanced(s):
    stack = []
    for character in s:
        if character in '[{(':
            stack.append(character)
        else:
            if not stack or stack.pop() != pair[character]:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

############################
# Without Dictionaries:
# def isBalanced(s):
#     brackets = ['()', '{}', '[]']
#
#     while any(bracket in s for bracket in brackets):
#         s = s.replace('()', '')
#         s = s.replace('{}', '')
#         s = s.replace('[]', '')
#
#     if s: # If there is still something in s, then it's unbalanced, thus return 'NO'
#         return 'NO'
#     return 'YES' # If s is empty after removing all paired parentheses, then return 'YES'

############################
# With Dictionaries (Annotated):
# PAIR = {')':'(','}':'{',']':'['}
#
# # Complete the isBalanced function below.
# def isBalanced(s):
#     stack = []
#     for char in s:
#         if char in '({[':
#             stack.append(char)
#         else:
#             if not stack or stack.pop() != PAIR[char]: # check if stack is empty (not stack = not empty) if not empty, then check if the stack.pop() character is paired properly, if not return No.
#
# # Pythonic language, 0 = False, all other integers = True; Empty list = False, Filled list = True
#                 return "NO"
#     if stack: # very pythonic, rather than saying, if len(stack) == 0
#         return "NO"
#     return "YES"

# ############################
# # LOCAL
# import sys # This is important to avoid differences in OS, this solution fails with default open() for file inputs
#
# pair = {')':'(','}':'{',']':'['}
#
# def isBalanced(s):
#     stack = []
#     for character in s:
#         if character in '[{(':
#             stack.append(character)
#         else:
#             if not stack or stack.pop() != pair[character]:
#                 return 'NO'
#     if stack:
#         return 'NO'
#     return 'YES'
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         s = input()
#
#         result = isBalanced(s)
#
#         print(result)
#
#         # fptr.write(result + '\n')
#
#     sys.stdin.close()