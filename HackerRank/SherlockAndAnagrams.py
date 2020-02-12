import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
# Generates all possible unique combinations from the string.
def gen_substrings(s):
    for i in range(1, len(s)): #Generate a window with size range()
        for j in range(len(s)-i+1): # start of index for window
            yield s[j:j+i]

# Tally up the totals from the unique combinations of the strings.
def sherlockAndAnagrams(s):
    anagrams_sorted = (''.join(sorted(string)) for string in gen_substrings(s))
    counts = Counter(anagrams_sorted)
    total = 0

    # A set of n anagramically-equivalent strings forms n(n-1)/2 pairs of strings
    for count in counts.values():
        total += count * (count - 1) / 2

    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

# ####### LOCAL
# #!/bin/python3
# import sys
# from collections import Counter
#
# # Complete the sherlockAndAnagrams function below.
# # Generates all possible unique combinations from the string.
# def gen_substrings(s):
#     for i in range(1, len(s)): #Generate a window with size range()
#         for j in range(len(s)-i+1): # start of index for window
#             yield s[j:j+i]
#
# # Tally up the totals from the unique combinations of the strings.
# def sherlockAndAnagrams(s):
#     anagrams_sorted = (''.join(sorted(string)) for string in gen_substrings(s))
#     counts = Counter(anagrams_sorted)
#     total = 0
#
#     for count in counts.values():
#         total += count * (count - 1) / 2
#
#     return int(total)
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     q = int(sys.stdin.readline())
#
#     for q_itr in range(q):
#         s = sys.stdin.readline()
#
#         result = sherlockAndAnagrams(s)
#
#         print(result)
