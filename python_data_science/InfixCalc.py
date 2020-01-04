from InfixToPostfix import infixToPostfix
from PostfixEval import postfixEval

def infixCalc(infixexpr):
    postfix = infixToPostfix(infixexpr)
    print("Postfix: ", postfix)
    ans = postfixEval(postfix)
    return ans

def main():
    print ("Enter postfix expression separated by space.")
    infixexpr = input("Expression: ")
    ans = infixCalc(infixexpr)
    print("Answer: ", ans)

if __name__ == '__main__':
    main()
