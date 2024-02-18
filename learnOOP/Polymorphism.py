import numpy as np
class Shape: #abstract class
    
    def calculateSurfaceArea(self): # different depending on subclass
        pass
    
    def calculatePerimeter(self): # different depending on subclass
        pass
    
    def draw(self): # changes depending on subclass
        pass

class Triangle(Shape):
    length1: float
    length2: float
    length3: float
    def __init__(self, l1 = 0.0, l2 = 0.0, l3 = 0.0):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
    
    
class Circle(Shape):
    radius: float
    def __init__(self, l1 = 0.0):
        self.radius = l1
    
    def calculateSurfaceArea(self):
        return np.pi * (self.radius ** 2)
    
    def calculatePerimeter(self):
        return np.pi * 2 * self.radius

class Rectangle(Shape):
    length1: float
    length2: float
    def __init__(self, l1, l2):
        self.length2 = l2
        self.length1 = l1
        
    def __init__(self, l1 = 0.0):
        self.__init__(l1, l1)
    
Shape s = Triangle()
