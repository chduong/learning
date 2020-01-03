class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None #grounds the initial node with 'next' set to None, which means that there is no next node.
        self.prev = None #for doubly linked list, pointer to previous Node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def setNext(self,newnext):
        self.next = newnext

    def isEmpty(self):  # checks to see if the list is empty
        return self.head == None  # None can be compared to any reference. Two references are equal if they both refer to the same object.

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head) #external link to current list
        self.head = temp #sets the new Node item as the new head

    def size(self):
        current = self.head
        count = 0
        while current != None: #!= is not equal python logic operator. While loop to count the items in the UnorderedList.
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:  # found is used as a boolean in addition to None to identify the end of the search (when an item is found and no more traversals are required)
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

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

    def append(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())  # external link to end of list
        current.setNext(temp)  # sets Node at current.getNext()

    def append_O1(self, item):
        if self.head is None:
            temp = Node(item)
            self.head = temp
            return
        n = self.head
        while n.next is not None:
            n = n.next
        temp = Node(item)
        n.next = temp
        temp.prev = n

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

    def __str__(self): #changes contents of object list to strings
        mylist_str = 'head'
        current = self.head
        while current != None:
            mylist_str = mylist_str + ' -> ' + str(current.getData())
            current = current.getNext()
        mylist_str = mylist_str + ' -> ' + str(None)
        return mylist_str

#Testing functions for Node
temp = Node(93)
print(temp.getData())

#Testing functions for UnorderedList
mylist = UnorderedList()

print('isEmpty =', mylist.isEmpty())

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print('size =', mylist.size())

print('search =', mylist.search(17))

mylist.remove(17)
print('mylist after remove=', mylist)

mylist.append(99)
print('mylist after append=', mylist)

mylist.append_O1(100)
print('mylist after append_O1=', mylist)

mylist.insert(5, 55)
print('mylist after insert=', mylist)

print('index =', mylist.index(55))

mylist.pop()
print('mylist after pop() =', mylist)

mylist.pop(0)
print('mylist after pop(pos)=', mylist)
