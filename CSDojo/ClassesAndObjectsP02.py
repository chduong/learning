# From ClassesAndObjectsP01.py
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print('My name is ' + self.name)

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 20)

class Person:
    def __init__(self, n, p, i, r): # n = name, p = personality, i = isSitting, r = robotOwned
        self.name = n
        self.personality = p
        self.isSitting = i
        self.robotOwned = r

# Changes the Boolean for the Person Sitting or Standing
    def sitDown(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False

# Assign Attributes for Person
p1 = Person('Alice', 'aggressive', False, r2)
p2 = Person('Bob', 'talkative', True, r1)

# Call On An Attribute By Robot Owned By Person.
p1.robotOwned.introduceSelf()
