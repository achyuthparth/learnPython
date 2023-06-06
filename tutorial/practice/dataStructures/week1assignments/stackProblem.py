#python3
#write a max method such that the running time is constant

import sys

class StackWithMax():
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
        assert(len(self.stack))
        return self.maxVal
    
    def pop(self):
        assert(len(self.stack))
        returnVal = self.stack[0]
        del self.stack[0]
        return returnVal
    
if __name__ == '__main__':
    stack = StackWithMax()

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


