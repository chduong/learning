# #!/bin/python3
import heapq
import sys

class priorityQueue(object):

    def __init__(self):
        self.arriving = []

    def load_customer(self, arrival, order_time):
        heapq.heappush(self.arriving, (arrival, order_time))

    def process_customer(self):  # minimumAverage(customers)
        instore = []
        total_wait = 0
        total_cust = 0
        now = 0

        while self.arriving or instore:
            # When no one is in the store, fast forward to the next arriving customer order
            if not instore and self.arriving[0][0] > now:
                now = self.arriving[0][0]

            # Load everyone who's shown up since the last pizza started cooking
            while self.arriving and self.arriving[0][0] <= now:
                arrival, order_time = heapq.heappop(self.arriving)
                heapq.heappush(instore, (order_time, arrival))

            # Handle customers in store and then return average wait time.
            order_time, arrival = heapq.heappop(instore)
            now += order_time
            total_wait += now - arrival
            total_cust += 1

        return total_wait // total_cust

if __name__ == '__main__':
    _ = sys.stdin.readline()

    pq = priorityQueue()

    for line in sys.stdin:
        pq.load_customer(*(int(row) for row in line.strip().split(' ')))
    print(pq.process_customer())

####### LOCAL
# import heapq
#
# class priorityQueue(object):
#
#     def __init__(self):
#         self.arriving = []
#
#     def load_customer(self, arrival, order_time):
#         heapq.heappush(self.arriving, (arrival, order_time))
#
#     def process_customer(self): # minimumAverage(customers)
#         instore = []
#         total_wait = 0
#         total_cust = 0
#         now = 0
#
#         while self.arriving or instore:
#             # When no one is in the store, fast forward to the next arriving customer order
#             if not instore and self.arriving[0][0] > now:
#                 now = self.arriving[0][0]
#
#             # Load everyone who's shown up since the last pizza started cooking
#             while self.arriving and self.arriving[0][0] <= now:
#                 arrival, order_time = heapq.heappop(self.arriving)
#                 heapq.heappush(instore, (order_time, arrival))
#
#         # Handle customers in store and then return average wait time.
#             order_time, arrival = heapq.heappop(instore)
#             now += order_time
#             total_wait += now - arrival
#             total_cust += 1
#
#         return total_wait // total_cust
#
# if __name__ == '__main__':
#     import sys
#
#     sys.stdin = open('data/input.txt', 'r')
#     _ = sys.stdin.readline()
#
#     pq = priorityQueue()
#
#     for line in sys.stdin:
#         pq.load_customer(*(int(row) for row in line.strip().split(' ')))
#     print(pq.process_customer())