import sys

class queue(object):
    def __init__(self):
        self.inbox = []
        self.q = []

    def enqueue(self, data):
        self.inbox.append(data)

    def dequeue(self):
        if not self.q:
            while self.inbox:
                self.q.append(self.inbox.pop())
        return self.q.pop()

    def peek(self):
        if not self.q:
            while self.inbox:
                self.q.append(self.inbox.pop())
        return self.q[-1]


if __name__ == '__main__':
    q = queue()
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split(' ')))
        if line[0] == 1:
            q.enqueue(line[1])
        elif line[0] == 2:
            q.dequeue()
        else:
            print(q.peek())

#######
# LOCAL
# import sys
#
# class queue(object):
#     def __init__(self):
#         self.inbox = []
#         self.q = []
#
#     def enqueue(self, data):
#         self.inbox.append(data)
#
#     def dequeue(self):
#         if not self.q:
#             while self.inbox:
#                 self.q.append(self.inbox.pop())
#         return self.q.pop()
#
#     def peek(self):
#         if not self.q:
#             while self.inbox:
#                 self.q.append(self.inbox.pop())
#         return self.q[-1]
#
# if __name__ == '__main__':
#     q = queue()
#     sys.stdin = open('data/input.txt', 'r')
#     n = int(input().strip())
#     for i in range(n):
#         line = list(map(int, input().split(' ')))
#         if line[0] == 1:
#             q.enqueue(line[1])
#         elif line[0] == 2:
#             q.dequeue()
#         else:
#             print(q.peek())