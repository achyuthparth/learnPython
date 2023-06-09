from linkedList import LinkedList

class Deque:
    def __init__(self):
        self.Deque = LinkedList()
        
    def getQueue(self):
        return self.Deque
    
    def enqueue(self, value):
        return LinkedList.pushValueBack(Deque.getQueue(self), value)
    
    def dequeue(self):
        return LinkedList.popFrontValue(Deque.getQueue(self))
    
    def push(self, value):
        return LinkedList.pushValueFront(Deque.getQueue(self), value)
    
    def top(self):
        return LinkedList.getHead(Deque.getQueue(self))
    
    #add tail to linked list and create bottom() method to return the tail just as top() returns the head
    
    def size(self):
        return LinkedList.size(Deque.getQueue(self))