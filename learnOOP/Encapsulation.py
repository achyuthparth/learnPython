# Encapsulation

class Car:
    model: str
    speed: int
    engine: int
    speedLimit: int
    def __init__(self, model, engine, speedLimit):
        self.model = model
        self.engine = engine
        self.speedLimit = speedLimit
    
    def drive(self):
        if self.speed != 0:
            self.speed = min(self.speed + 10, self.speedLimit)
        else: self.speed = 10
    
    def stop(self):
        self.speed = 0
        return
    
    def setSpeed(self, number):
        self.speed = min(number, self.speedLimit) # when we override, we might want to keep the caller informed so we return self.speed
        return self.speed # this is called user empathy
    
        # enter validations
        # additional processes
        # encapsulation functions act on the data members of the class instead of all users being able to manipulate

class Cat:
    mood: int
    hungry: bool
    energy: int
    
    def __init__(self):
        self.mood = 0
        self.hungry = False
        self.energy = 0
    
    def __meow(self): # this is private, only this class can call
        self.__meow("meow")
        
    def __meow(self, sound):
        print(sound)
    
    def feed(self):
        if self.hungry == False:
            return
        self.hungry = False
        self.energy += 20
        self.mood += 1
        self.__meow()
    # use methods to manipulate attributes instead of changing directly
    
    def play(self):
        # energy exception if insufficient
        self.hungry = True
        self.energy -= 20
        self.mood += 10
        self.__meow()
        
# use class slides pdf to create examples with assistance of the textbook
    def sleep(self):
        self.energy = 80
        self.hungry = True
        self.mood = 70
        
cat1 = Cat()

cat1.play()