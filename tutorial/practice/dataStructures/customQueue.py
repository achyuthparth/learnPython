from linkedList import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()
        
    def getQueue(self):
        return self.queue
    
    def enqueue(self, value):
        return LinkedList.pushValueBack(Queue.getQueue(self), value)
    
    def dequeue(self):
        return LinkedList.popFrontValue(Queue.getQueue(self))
    
    def top(self):
        return LinkedList.getHead(Queue.getQueue(self))
    
    def size(self):
        return LinkedList.size(Queue.getQueue(self))