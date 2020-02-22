#!/bin/python3

import os
from collections import defaultdict

# Complete the bfs function below.
def generate_graph(edges):
    graph = defaultdict(list)
    for node1, node2 in edges:
        # Bidirectional BFS (unidirectional fails)
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def find_distances(s, graph):
    q = [s]
    distances = defaultdict(lambda: -1) # Specifies the default dictionary key returns -1
    distances[s] = 0
    weight = 6

    # Computes edge weighted distances from starting node
    while q:
        node = q.pop(0)

        # Process the nodes and for any adjacent nodes, calculate the distances for that node from the starting node.
        for adjacent_node in graph[node]:
            if distances[adjacent_node] == -1:
                distances[adjacent_node] = distances[node] + weight
                q.append(adjacent_node)
    return distances

def bfs(n, m, edges, s):
    graph = generate_graph(edges)
    distances = find_distances(s, graph)

    return [distances[node] for node in range(1, n + 1) if node != s]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


####### LOCAL
# import sys
# from collections import defaultdict
#
# # Complete the bfs function below.
# def generate_graph(edges):
#     graph = defaultdict(list)
#     for node1, node2 in edges:
#         # Bidirectional BFS (unidirectional BFS fails test cases)
#         graph[node1].append(node2)
#         graph[node2].append(node1)
#     return graph
#
# def find_distances(s, graph):
#     q = [s]
#     distances = defaultdict(lambda: -1) # Specifies the default dictionary key returns -1
#     distances[s] = 0
#     weight = 6
#
#     # Computes edge weighted distances from starting node
#     while q:
#         node = q.pop(0)
#
#         # Process the nodes and for any adjacent nodes, calculate the distances for that node from the starting node.
#         for adjacent_node in graph[node]:
#             if distances[adjacent_node] == -1:
#                 distances[adjacent_node] = distances[node] + weight
#                 q.append(adjacent_node) # For computing distances of nodes > 1 adjacent node
#     return distances
#
# def bfs(n, m, edges, s):
#     graph = generate_graph(edges)
#     distances = find_distances(s, graph)
#
#     return [distances[node] for node in range(1, n + 1) if node != s]
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     q = int(sys.stdin.readline())
#
#     for q_itr in range(q):
#         nm = sys.stdin.readline().split()
#
#         n = int(nm[0])
#
#         m = int(nm[1])
#
#         edges = []
#
#         for _ in range(m):
#             edges.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
#         s = int(sys.stdin.readline())
#
#         result = bfs(n, m, edges, s)
#
#         print(result)
