import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = {} # create dictionary
    for color1 in ar:
        count = 0
        for color2 in ar:
            if color1 == color2:
                count += 1
        colors[color1] = count #adds key, value to dictionary, in this case color1, count

    pairs = 0
    for color in colors: # color = key
        pairs += colors[color] // 2 # color = key, colors[color] = key's value
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

####################################
# # LOCAL
# # Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#     colors = {}
#     for color1 in ar:
#         count = 0
#         for color2 in ar:
#             if color1 == color2:
#                 count += 1
#         colors[color1] = count
#
#     pairs = 0
#     for color in colors: # color = key
#         pairs += colors[color] // 2 # color = key, colors[color] = count
#     return pairs
#
# if __name__ == '__main__':
#     fptr = open('data/input.txt', 'r')
#
#     n = int(fptr.readline())
#
#     ar = list(map(int, fptr.readline().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.close()
