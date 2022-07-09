
def Fn(name, x):
    if (x > 5):
        return

    str = "name is " + name
    print(str)
    Fn(name, x+1)

Fn("acb", 1)



def Fib(p2, p1):
    if p1 > 100:
        return

    print(p1)

    Fib(p1, p1 + p2)


Fib(0, 1)


def Staircase(num):
    cache = list()
    return Staircase(num, cache)


def Starcase(num, cache):

    if (num + 2 == 20):
        cache.append(2)
        return cache

    if (num + 1 == 20):
        cache.append(1)
        return cache

    if (num < 0):
        return cache

    else:
        Staircase(num -1, cache)



