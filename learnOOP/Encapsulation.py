# Encapsulation

class Car:
    type: str
    cylinderCount: int
    doorCount: int
    def __init__(self, engine):
        self.engine = engine
        
    def replaceEngine(self, engine, cylinderCount):
        self.cylinderCount = cylinderCount
        self.engine = engine
        # enter validations
        # additional processes
        # encapsulation functions act on the data members of the class instead of all users being able to manipulate

carVariable = Car("v8")
carVariable.cylinderCount = 8

class Cat:
    mood: str
    hungry: bool
    energy: int
    def meow():
        return
    
    def eat(self):
        if self.hungry == False:
            return
        self.hungry = False
        self.energy += 20
        self.mood = "happy"
    # use methods to manipulate attributes instead of changing directly
    
    def runAMile(self):
        # energy exception if insufficient
        self.hungry = True
        self.energy -= 20
        self.mood = "tired"
        
# use class slides pdf to create examples with assistance of the textbook