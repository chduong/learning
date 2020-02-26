import numpy as np
import math

#Process the input and output
def main():
    sys.stdin = open('data/input.txt', 'r')
    N = int(input())
    for _ in range(N):
        input()
        ratings = [float(i) for i in input().strip().split()]
        corrs = [pearsonCorr(ratings, [float(i) for i in input().strip().split()]) for j in range(5)]
        print(np.argmax(corrs) + 1) # + 1 for 1 indexing

# Pearson Correlation Coefficient Defined Here:
# https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
def sumSquares(x, y):
    return sum(i * j for (i, j) in zip(x, y)) / len(x) - (sum(x) * sum(y)) / len(x)**2

def pearsonCorr(x, y):
    try:
        correlation = sumSquares(x, y) / math.sqrt(abs(sumSquares(x, x) * sumSquares(y, y)))
    except Exception:
        correlation = 0
    return correlation

if __name__ == "__main__":
    main()

####### Using sklearn
# from sklearn.linear_model import LinearRegression
# import numpy as np
# T = int(input())
# for _ in range(T):
#     lr = LinearRegression()
#     _ = int(input())
#     y = list(map(float,input().strip().split()))
#     X = []
#     for _ in range(5):
#         X.append(list(map(float,input().strip().split())))
#     XX = np.array(X).T
#     lr.fit(XX,y)
#     print( np.argmax(lr.coef_)+1)

####### Using scipy.stats
# from scipy.stats import pearsonr
# import math
# def bestTest(N, gpas, test_results):
#     results = []
#     for scores in test_results:
#         results.append((0,0) if math.isnan(pearsonr(scores, gpas)[0]) else pearsonr(scores, gpas))
#     highest_test = results.index(max(results)) + 1
#     return highest_test
# if __name__ == '__main__':
#     T = int(input())
#     for _ in range(T):
#         N = int(input())
#         gpas = list(map(float, input().split()))
#         test_results = []
#         for _ in range(5):
#             test_results.append(list(map(float, input().split())))
#         print(bestTest(N, gpas, test_results))

####### LOCAL
# import sys
# import numpy as np
# import math
#
# #Process the input and output
# def main():
#     sys.stdin = open('data/input.txt', 'r')
#     N = int(input())
#     for _ in range(N):
#         input()
#         ratings = [float(i) for i in input().strip().split()]
#         corrs = [pearsonCorr(ratings, [float(i) for i in input().strip().split()]) for j in range(5)]
#         print(np.argmax(corrs) + 1) # + 1 for 1 indexing
#
# # Pearson Correlation Coefficient Defined Here:
# # https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
# def sumSquares(x, y):
#     return sum(i * j for (i, j) in zip(x, y)) / len(x) - (sum(x) * sum(y)) / len(x)**2
#
# def pearsonCorr(x, y):
#     try:
#         correlation = sumSquares(x, y) / math.sqrt(abs(sumSquares(x, x) * sumSquares(y, y)))
#     except Exception:
#         correlation = 0
#     return correlation
#
# if __name__ == "__main__":
#     main()