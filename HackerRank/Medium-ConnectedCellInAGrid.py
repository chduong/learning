#!/bin/python3

import os

# Complete the connectedCell function below.
def connectedCell(matrix):
    n = len(matrix)

    # copy of original matrix filled with False to track what's been visited
    m = len(matrix[0])

    visited = [[False for j in range(m)] for i in range(n)]
    maxSize = 0

    def dfs(i, j):
        size = 1
        visited[i][j] = True
        for p in range(i-1, i + 2):
            for q in range(j-1, j + 2):
                if p >= 0 and p < n and q >= 0 and q < m and (p != i or q != j):
                    if visited[p][q] == False and matrix[p][q] == 1:
                        size += dfs(p, q)
        return size

    for i in range (n):
        for j in range(m):
            if matrix [i][j] == 1 and not visited[i][j]:
                maxSize = max(maxSize, dfs(i, j))
    return maxSize

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()


# ####### LOCAL
# import sys
#
# # Complete the connectedCell function below.
# # Recursive Depth First Search
# def connectedCell(matrix):
#     n = len(matrix)
#
#     # copy of original matrix filled with False to track what's been visited
#     m = len(matrix[0])
#
#     visited = [[False for j in range(m)] for i in range(n)]
#     maxSize = 0
#
#     def dfs(i, j):
#         size = 1
#         visited[i][j] = True
#         for p in range(i-1, i + 2):
#             for q in range(j-1, j + 2):
#                 if p >= 0 and p < n and q >= 0 and q < m and (p != i or q != j):
#                     if visited[p][q] == False and matrix[p][q] == 1:
#                         size += dfs(p, q)
#         return size
#
#     for i in range (n):
#         for j in range(m):
#             if matrix [i][j] == 1 and not visited[i][j]:
#                 maxSize = max(maxSize, dfs(i, j))
#     return maxSize
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     n = int(input())
#
#     m = int(input())
#
#     matrix = []
#
#     for _ in range(n):
#         matrix.append(list(map(int, input().rstrip().split())))
#
#     result = connectedCell(matrix)
#
#     print(result)
