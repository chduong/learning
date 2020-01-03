class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None: #for when the item is added to the top of the list
            temp.setNext(self.head)
            self.head = temp
        else: #for when the item is added to the middle of the list
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None #returns True or False Boolean

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current  # move 'previous' first, otherwise if 'previous' moves second, it will move to where 'current' moved to, instead of where 'current' is currently.
                current = current.getNext()
        if previous == None:  # if the removal item is at the head
            self.head = current.getNext()
        else:  # if the removal item is in the middle
            previous.setNext(current.getNext())

    def __str__(self): #changes contents of object list to strings
        mylist_str = 'head'
        current = self.head
        while current != None:
            mylist_str = mylist_str + ' -> ' + str(current.getData())
            current = current.getNext()
        mylist_str = mylist_str + ' -> ' + str(None)
        return mylist_str

    def index(self, item):
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def insert(self, index, item):
        current = self.head
        for i in range(index):
            current = current.getNext()

        if current !=None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise('Index out of Range')

    def pop(self, index=''):
        current = self.head
        if index != '': #for pop(pos)
            for i in range(index):
                current = current.getNext()
            if current != None:
                temp = current.getData()
                self.remove(temp)
            else:
                raise('Index out of range')
        else: #for pop()
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            if current.getNext() == None:
                temp = current.getData()
                self.remove(temp)

#Testing functions for OrderedList
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print('size =', mylist.size())
print('search 93 =', mylist.search(93))
print('search 1000 =', mylist.search(1000))
print('remove 93 =', mylist.remove(93))
print(mylist)
print('index 17 =', mylist.index(17))
mylist.insert(1, 7)
print('insert 7=', mylist)
mylist.pop()
print('pop =', mylist)
mylist.pop(0)
print('pop(pos) =', mylist)
