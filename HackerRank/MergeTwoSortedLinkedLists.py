# Python 3
# No stdin/out, all inputs/outputs handled by system

# !/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000)

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


class Node(object):
    def __init__(self, data = None, next_node=None):
        self.data = data
        self.next = next_node

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data <= head2.data:
        head1.next = mergeLists(head1.next, head2)
        return head1
    head2.next = mergeLists(head1, head2.next)
    return head2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()


#######
# Iterative Solution:
# def mergeLists(head1, head2):
#     # Setup a dummy for returning the head of the merged list
#     dummy = SinglyLinkedListNode('#')
#     cur = dummy
#     while head1 and head2:
#         if head1.data <= head2.data:
#             cur.next = head1
#             head1 = head1.next
#         else:
#             cur.next = head2
#             head2 = head2.next
#         cur = cur.next
#     if head1:
#         cur.next = head1
#     if head2:
#         cur.next = head2
#     return dummy.next

#######
# LOCAL

# import math
# import os
# import random
# import re
# import sys
# sys.setrecursionlimit(10000)
#
# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def insert_node(self, node_data):
#         node = SinglyLinkedListNode(node_data)
#
#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node
#
#         self.tail = node
#
# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         print(str(node.data), end=' ')
#
#         node = node.next
#
# class Node(object):
#     def __init__(self, data = None, next_node=None):
#         self.data = data
#         self.next = next_node
#
# # Complete the mergeLists function below.
#
# def mergeLists(head1, head2):
#     if head1 == None:
#         return head2
#     if head2 == None:
#         return head1
#     if head1.data <= head2.data:
#         head1.next = mergeLists(head1.next, head2)
#         return head1
#     head2.next = mergeLists(head1, head2.next)
#     return head2
#
#
# if __name__ == '__main__':
#     sys.stdin = open('data/input.txt', 'r')
#
#     tests = int(input())
#
#     for tests_itr in range(tests):
#         llist1_count = int(input())
#
#         llist1 = SinglyLinkedList()
#
#         for _ in range(llist1_count):
#             llist1_item = int(input())
#             llist1.insert_node(llist1_item)
#
#         llist2_count = int(input())
#
#         llist2 = SinglyLinkedList()
#
#         for _ in range(llist2_count):
#             llist2_item = int(input())
#             llist2.insert_node(llist2_item)
#
#         llist3 = mergeLists(llist1.head, llist2.head)
#
#         print_singly_linked_list(llist3, ' ', sys.stdin)
#
#     sys.stdin.close()