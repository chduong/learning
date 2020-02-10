import sys
import os
import heapq

def add_entry(smalls, larges, v):
    if not smalls:
        smalls.append(-v)
        return None  # or 'return' is equivalent
    if -smalls[0] < v:
        heapq.heappush(larges, v)
    else:
        heapq.heappush(smalls, -v)

    if len(smalls) > len(larges) + 1:
        heapq.heappush(larges, -heapq.heappop(smalls))
    elif len(smalls) < len(larges):
        heapq.heappush(smalls, -heapq.heappop(larges))


def runningMedian(smalls, larges):
    if len(smalls) == len(larges):
        return (-smalls[0] + larges[0]) / 2.0
    else:
        return -smalls[0]


if __name__ == '__main__':
    _ = int(sys.stdin.readline())

    smalls = []
    larges = []

    for line in sys.stdin:
        add_entry(smalls, larges, int(line.strip()))
        print('%0.1f' % runningMedian(smalls, larges))

# Sort Heap:
# def heapsort(heap):
#     return [heapq.heappop(heap) for _ in range(len(heap))]

####### LOCAL
# import sys
# import os
# import heapq
#
# def add_entry(smalls, larges, v):
#     if not smalls:
#         smalls.append(-v)
#         return None  # or 'return' is equivalent
#     if -smalls[0] < v:
#         heapq.heappush(larges, v)
#     else:
#         heapq.heappush(smalls, -v)
#
#     if len(smalls) > len(larges) + 1:
#         heapq.heappush(larges, -heapq.heappop(smalls))
#     elif len(smalls) < len(larges):
#         heapq.heappush(smalls, -heapq.heappop(larges))
#
#
# def runningMedian(smalls, larges):
#     if len(smalls) == len(larges):
#         return (-smalls[0] + larges[0]) / 2.0
#     else:
#         return -smalls[0]
#
#
# if __name__ == '__main__':
#     import sys
#
#     sys.stdin = open('data/input.txt', 'r')
#
#     _ = int(sys.stdin.readline())
#
#     smalls = []
#     larges = []
#
#     for line in sys.stdin:
#         add_entry(smalls, larges, int(line.strip()))
#         print('%0.1f' % runningMedian(smalls, larges))
#
#     sys.stdin.close()