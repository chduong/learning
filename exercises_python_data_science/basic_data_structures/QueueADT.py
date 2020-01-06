# ######################################
# # List Programming Exercise 5 Implement Queue Abstract Data Type (Queue ADT)
# ######################################
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if item not in self.items:
            self.items.insert(0, item)
            return (item, 'Added to Queue')
        else:
            return (item, 'Already in Queue')

    def dequeue(self):
        if self.items != []:
            return (self.items.pop(), 'Removed from Queue')
        else:
            return ('Queue is Empty')

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(5))
print(q.enqueue(7))

print('size =', q.size())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print('size after dequeue =', q.size())

print(q.dequeue())

print('size after dequeue 2 =', q.size())

print(q.dequeue())