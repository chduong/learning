from pythonds.basic import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,11) # average length of pages cut in half, from 20 to 10

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute, secondsPerTask):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask(secondsPerTask):
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask(secondsPerTask):
    num = random.randrange(1, secondsPerTask+1) # Twice as many students, means less time between tasks
    if num == secondsPerTask:
        return True
    else:
        return False

num_students = 20
tasksPerSecond = (2*num_students)*(1/60)*(1/60) #Number of tasks per hour converted to tasks per second
secondsPerTask = int(1/tasksPerSecond) #python math made it 90.00000000000001, so int() was required to make it a whole number for newPrintTask to work.
for i in range(10): # number of trials
    simulation(3600, 5, secondsPerTask) # parameters are: number of simulations per second, number of pages printed per minute
