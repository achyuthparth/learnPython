class Figure: #abstract class
    
    def calculateSurface(): # different depending on subclass
        return
    
    def calculatePerimeter(): # different depending on subclass
        return
    

class Triangle:
    length1: float
    length2: float
    length3: float
    def __init__(self, l1 = 0.0, l2 = 0.0, l3 = 0.0):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3

class Circle:
    radius: float
    def __init__(self, l1 = 0.0):
        self.radius = l1

class Rectangle:
    length1: float
    length2: float
    def __init__(self, l1 = 0.0):
        self.length1 = l1
        self.length2 = l1
    
    def __init__(self, l1, l2):
        self.length2 = l2
        self.length1 = l1


class Vehicle:
    def startEngine(self):
        return # set up for different subclasses
    
class Scooter(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass