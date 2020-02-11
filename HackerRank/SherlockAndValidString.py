from collections import Counter
import sys

# Complete the isValid function below.
def isValid(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    #For case when all characters have the same frequency
    if len(freq_count) == 1:
        return 'YES'

    #The only other condition to establish are the cases for when there are two different frequencies, but removing one item yields a uniform frequency.
    elif len(freq_count) == 2:

        # Case for when the keys are 1 apart and the max frequency count of one key is 1
        freq_key = freq_count.keys()
        if max(freq_key) - min(freq_key) == 1 and freq_count[max(freq_key)] == 1:
            return 'YES'

        # Case for when the keys are not 1 apart and the max frequency count of one key is 1
        elif (1, 1) in freq_count.items():
            return 'YES'

        else:
            return 'NO'

    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

####### FROM richardlamb1985, not using collections
# def isValid(s):
#     #Create a list containing just counts of each distinct element
#     freq = [s.count(letter) for letter in set(s) ]
#     #If all values the same, then return 'YES'
#     if max(freq)-min(freq) == 0:
#         return 'YES'
#     #If difference between highest count and lowest count is 1
#     #and there is only one letter with highest count,
#     #then return 'YES' (because we can subtract one of these
#     #letters and max=min , i.e. all counts are the same)
#     elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
#         return 'YES'
#     #If the minimum count is 1
#     #then remove this letter, and check whether all the other
#     #counts are the same
#     elif freq.count(min(freq)) == 1 and min(freq) == 1:
#         freq.remove(min(freq))
#         if max(freq)-min(freq) == 0:
#             return 'YES'
#         else:
#             return 'NO'
#     else:
#         return 'NO'

####### LOCAL
#!/bin/python3

# from collections import Counter
# import sys
#
# # Complete the isValid function below.
# def isValid(s):
#     char_count = Counter(s)
#     freq_count = Counter(char_count.values())
#
#     #For case when all characters have the same frequency
#     if len(freq_count) == 1:
#         return 'YES'
#
#     #The only other condition to establish are the cases for when there are two different frequencies, but removing one item yields a uniform frequency.
#     elif len(freq_count) == 2:
#
#         # Case for when the keys are 1 apart and the max frequency count of one key is 1
#         freq_key = freq_count.keys()
#         if max(freq_key) - min(freq_key) == 1 and freq_count[max(freq_key)] == 1:
#             return 'YES'
#
#         # Case for when the keys are not 1 apart and the max frequency count of one key is 1
#         elif (1, 1) in freq_count.items():
#             return 'YES'
#
#         else:
#             return 'NO'
#
#     else:
#         return 'NO'
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     s = sys.stdin.readline()
#
#     result = isValid(s)
#
#     print(result)
