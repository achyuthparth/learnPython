#python3
#write a max method such that the running time is constant

import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.maxVal = None
        
    def push(self, value):
        if len(self.stack) <= self.size:
            if self.maxVal is None or self.maxVal < value:
                self.maxVal = value
            self.stack.insert(0, value)
            
    def max(self):
        return self.maxVal
    
    def pop(self):
        returnVal = self.stack[0]
        del self.stack[0]
        return returnVal

if __name__ == '__main__':
    stack = Stack()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert(0)


