# ######################################
# # List Programming Exercise 4 Build an Infix Calculator
# ######################################
from InfixCalc import infixCalc

def calculator():
    while True:
        infixexpr = input("Expression: ")
        ans = infixCalc(infixexpr)
        print("Answer: ", ans)
        print("press any key to continue, \'n\' to exit.")
        keystroke = input()
        if keystroke == 'n':
            break

def main():
    calculator()

if __name__ == '__main__':
    main()