# ######################################
# # List Programming Exercise 1 Infix to Postfix Evaluation Error Handling
# ######################################
# requires: pip install pythonds
from pythonds.basic import Stack

def validateInput(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count != 0:
        print('Check Parentheses')
        return False
    return count == 0

def infixToPostfix(infixexpr):
    if validateInput(infixexpr) != False:
        prec = {}
        prec["**"] = 4
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = Stack()
        postfixList = []
        tokenList = infixexpr.split()

        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)
    else:
        return False

print(infixToPostfix("A * B + C * D")) #correct
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")) #correct

print(validateInput("A * B + C * D")) #correct

print(validateInput("(A * B + C * D")) #extra parentheses

print(infixToPostfix("5 * 3 ** ( 4 - 2 )")) #correct

print(infixToPostfix("(5 * 3 ** ( 4 - 2 )")) #extra parentheses
