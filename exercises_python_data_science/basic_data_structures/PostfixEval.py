# ######################################
# # List Programming Exercise 2 Postfix Evaluation Error Handling
# ######################################
# requires: pip install pythonds
from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            # Error Handling Code
            if operandStack.size() < 2:
                print ('Invalid postfix expression, please correct the input.')
                return None
            #
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "**":
        return op1 ** op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# print(postfixEval('7 8 + 3 2 + /'))
# print(postfixEval('5 3 4 2 - ** *'))
#
# print(postfixEval('5 3 4 2 + - ** *'))