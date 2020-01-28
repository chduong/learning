# Recursively selects the final value in the array as the partition, then sorts all values with respect the partition, then swaps the partition into the proper position and sorts the two halves of the partition with respect to the final values within each subpartition and then continues until all values are sorted.
import sys
# Like Python indexing, lo to hi-1
def partition(arr, lo, hi):
    pivot_val = arr[hi - 1]
    j = lo
    for i in range(lo, hi-1):
        if arr[i] < pivot_val:
            arr[i], arr[j] = arr[j], arr[i] # j is stationary until arr[i] is true for the inequality condition, then it switches arr[i] and arr[j]
            j += 1
    arr[hi-1], arr[j] = arr[j], arr[hi-1]
    print(" ".join([str(arr[i]) for i in range(len(arr)) ] ) )
    return j

def quicksort(arr, lo=0, hi=-1):
    if hi == -1:
        hi = len(arr)
    if lo < hi - 1:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)

if __name__ == '__main__':
    import sys
    _ = sys.stdin.readline()
    quicksort([int(i) for i in sys.stdin.readline().split(' ')])

#####################################
# General Idea from Wikipedia:
# algorithm quicksort(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort(A, lo, p - 1)
#         quicksort(A, p + 1, hi)
#
# algorithm partition(A, lo, hi) is
#     pivot := A[hi]
#     i := lo
#     for j := lo to hi do
#         if A[j] < pivot then
#             swap A[i] with A[j]
#             i := i + 1
#     swap A[i] with A[hi]
#     return i

#####################################
# # from rdm750 (HackerRank)
# def quicksort(ar, lo, hi):
#     if lo < hi:
#         p = partition(ar, lo, hi)
#         print
#         ' '.join(map(str, ar))
#         quicksort(ar, lo, p - 1)
#         quicksort(ar, p + 1, hi)
#
#     else:
#         return
#
# def partition(A, lo, hi):
#     pivot = A[hi]
#     i = lo  # place for swapping
#     for j in xrange(lo, hi):
#         if A[j] <= pivot:
#             x = A[i]
#             A[i] = A[j]
#             A[j] = x
#             i += 1
#     x = A[i]
#     A[i] = A[hi]
#     A[hi] = x
#     left, right = [], []
#
#     return i
#
# m = input()
# ar = [int(i) for i in raw_input().strip().split()]
#
# quicksort(ar, 0, len(ar) - 1)
#####################################
# # LOCAL
# import sys
# # Like Python indexing, lo to hi-1
# def partition(arr, lo, hi):
#     pivot_val = arr[hi - 1]
#     j = lo
#     for i in range(lo, hi-1):
#         if arr[i] < pivot_val:
#             arr[i], arr[j] = arr[j], arr[i] # j is stationary until arr[i] is true for the inequality condition, then it switches arr[i] and arr[j]
#             j += 1
#     arr[hi-1], arr[j] = arr[j], arr[hi-1]
#     print(" ".join([str(arr[i]) for i in range(len(arr)) ] ) )
#     return j
#
# def quicksort(arr, lo=0, hi=-1):
#     if hi == -1:
#         hi = len(arr)
#     if lo < hi - 1:
#         p = partition(arr, lo, hi)
#         quicksort(arr, lo, p)
#         quicksort(arr, p + 1, hi)
#
# if __name__ == '__main__':
#     import sys
#     sys.stdin = open('data/input.txt', 'r')
#     _ = sys.stdin.readline()
#     quicksort([int(i) for i in sys.stdin.readline().split(' ')])