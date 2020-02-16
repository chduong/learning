#!/bin/python3

import sys
from collections import defaultdict

def cutTheTree(data, edges):
    nodes = len(data)
    total = sum(data)
    min_cut = total

    graph = addEdges(edges)
    parent_nodes, order = breadthFirstSearch(graph, nodes)

    while order:
        node = order.pop()

        # tree1 = total - data[node]
        # node_cut = abs(tree1 - data[node])
        node_cut = abs(total - 2 * data[node])
        if node_cut < min_cut:
            min_cut = node_cut
        data[parent_nodes[node]] += data[node]
    return min_cut


def addEdges(edges):
    graph = defaultdict(list)

    for u, v in edges:
        # Impose 0 indexing for convenience
        # Allows for traversal in both directions of edges
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    return graph


# Breadth first search algorithm to find parent-child relationship.
def breadthFirstSearch(graph, nodes):
    visted_nodes = [False] * nodes
    queue = [0]

    for index in range(nodes):
        node = queue[index]
        for adjacent_node in graph[node]:
            if visted_nodes[adjacent_node] is False:
                queue.append(adjacent_node)
                visted_nodes[adjacent_node] = node
    return visted_nodes, queue


if __name__ == '__main__':
    sys.stdin = open('data/input.txt', 'r')

    n = int(sys.stdin.readline().strip())

    data = list(map(int, sys.stdin.readline().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = cutTheTree(data, edges)
    print(result)