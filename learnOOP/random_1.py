#is duck

def is_duck(object):
    return bool(
        hasattr(object, "walk")
        and callable(object.walk)
        and hasattr(object, "quack")
        and callable(object.quack)
    )

class FakeDuck:
    pass

class Duck:
    def walk(self):
        return
    def quack(self):
        return
    
duck = Duck()
fDuck = FakeDuck()

print(is_duck(duck))
print(is_duck(fDuck))
