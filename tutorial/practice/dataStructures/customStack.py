from linkedList import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()
        
    def getStack(self):
        return self.stack
    
    def push(self, value):
        return LinkedList.pushValueFront(Stack.getStack(self), value)
    
    def pop(self):
        return LinkedList.popFrontNode(Stack.getStack(self))
    
    def top(self):
        return LinkedList.getHead(Stack.getStack(self))
    
    def size(self):
        return LinkedList.size(Stack.getStack(self))