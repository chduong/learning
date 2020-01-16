import time
start_time = time.time()

def minion_game(string):
    vowel = 'AEIOU'
    stuart_score = 0
    kevin_score = 0

    # shortens solution from O(n^2) to O(n) by just giving the person the score that totals up the length of the string at that given letter
    # for i, char in enumerate(string), complexity O(n) operation): #slower than range(len(string)), complexity O(1)
    for i in range(len(string)):
        if string[i] in vowel:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print('Stuart {a}'.format(a=stuart_score))
    elif stuart_score < kevin_score:
        print('Kevin {a}'.format(a=kevin_score))
    elif stuart_score == kevin_score:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

print("--- %s seconds ---" % (time.time() - start_time))
#######################################
# By Slaunger:
# def minion_game(s):
#     V = frozenset("AEIOU")
#     n = len(s)
#     ksc = sum(q for c, q in zip(s, range(n, 0, -1)) if c in V)
#     ssc = n * (n + 1) // 2 - ksc
#     if ksc > ssc:
#         print("Kevin {:d}".format(ksc))
#     elif ssc > ksc:
#         print("Stuart {:d}".format(ssc))
#     else:
#         print("Draw")
#
# Several optimizations.
#
# 1. Use frozenset for the vowels. This is the fastest to lookup in.
# 2. Iterate through characters instead of indexing
# 3. Iterate q reverse to avoid a subtraction in each sum
# 4. Avoid repeated calls to len
# 5. Only calculate Kevins score the hard way. Use the fact that the total number of substrings is n * (n + 1) / 2 and find Stuart's score by subtracting Kevin's from the total number of substrings.

#######################################

# Slightly faster? by mandos9, enumerate over o reverse:
# def minion_game(string):
#     vowels = frozenset("AIEOU")
#     lens = len(string)
#
#     kevin = sum( i for i, c in enumerate(reversed(string)) if c in vowels) + lens
#     stuart = ( lens * (lens + 1) ) // 2 - kevin
#
#     if stuart > kevin:
#         print(f"Stuart {stuart}")
#     elif kevin > stuart:
#         print(f"Kevin {kevin}")
#     else:
#         print("Draw")

#######################################
# By Alphasingh, updated by Bradm124 for Python 3 (Short, but less readable code)
#
#     s = string
#     vowels, L = 'AEIOU', len(s)
#     K = sum([L-i for i in range(L) if s[i] in vowels])
#     S = sum([L-i for i in range(L) if s[i] not in vowels])
#     print(['Stuart '+str(S),['Kevin '+str(K),'Draw'][K==S]][K>=S])