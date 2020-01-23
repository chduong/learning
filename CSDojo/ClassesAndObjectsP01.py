class Robot:
    def introduceSelf(self):
        print('My name is ' + self.name)

# Assign Robot Attributes
r1 = Robot()
r1.name = 'Tom'
r1.color = 'red'
r1.weight = 30

# Make a Second Robot
r2 = Robot()
r2.name = 'Jerry'
r2.color = 'green'
r2.weight = 20

r1.introduceSelf()
r2.introduceSelf()

# Build a Constructor Into the Class
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print('My name is ' + self.name)

# r1.name, r1.color, r1.weight No Longer Work

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 20)

r1.introduceSelf()
r2.introduceSelf()