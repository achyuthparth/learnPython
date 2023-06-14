from math import inf as infinity

def Swap(heapArray, position1, position2):
    heapArray[position1], heapArray[position2] = heapArray[position2], heapArray[position1]
    return heapArray

class MaxHeap:
    #maxSize
    #currentSize
    #h, array which stores the heap
    #1 based index instead of 0 to make parent and child operations easier
    
    def __init__(self, maxSize = 1, currentSize = 0):
        self.maxSize = maxSize
        self.currentSize = currentSize
        self.maxHeapArray = [None] * (self.maxSize)
    
    
    def Parent(index):
        return (index - 1) // 2
    
    def LeftChild(index):
        return 1 + (index * 2)
    
    def RightChild(index):
        return 2 + (index * 2)
    
    def GetMax(self):
        return self.maxHeapArray[0]
    
    def SiftUp(self, index):
        while index > 1 and self.maxHeapArray[MaxHeap.Parent(index)] < self.maxHeapArray[index]:
            Swap(self.maxHeapArray, self.maxHeapArray[MaxHeap.Parent(index)], self.maxHeapArray[index])
            index = MaxHeap.Parent(index)
    
    def SiftDown(self, index):
        maxIndex = index
        left = MaxHeap.LeftChild(index)
        if left <= self.currentSize and self.maxHeapArray[left] > self.maxHeapArray[maxIndex]:
            maxIndex = left
        
        right = MaxHeap.RightChild(index)
        if right <= self.currentSize and self.maxHeapArray[right] > self.maxHeapArray[maxIndex]:
            maxIndex = right
        
        if index != maxIndex:
            Swap(self.maxHeapArray, self.maxHeapArray[index], self.maxHeapArray[maxIndex])
            MaxHeap.SiftDown(self, maxIndex)
    
    def Insert(self, priority):
        #if array size is constant return error below
        '''
        if self.currentSize == self.maxSize:
            raise Exception("heap full")
        '''
        #if array size is mutable perform below
        if self.currentSize == self.maxSize:
            self.maxSize += 1
            self.maxHeapArray.append(None)
        self.currentSize += 1
        self.maxHeapArray[self.currentSize] = priority
        MaxHeap.SiftUp(priority)
    
    def ExtractMax(self):
        result = self.maxHeapArray[0]
        self.maxHeapArray[0] = self.maxHeapArray[self.currentSize]
        self.currentSize -= 1
        MaxHeap.SiftDown(self, 0)
        return result
    
    def Remove(self, index):
        self.maxHeapArray[index] = infinity
        MaxHeap.SiftUp(self, index)
        MaxHeap.ExtractMax(self)
    
    def ChangePriority(self, index, priority):
        oldPrioroty = priority
        self.maxHeapArray[index] = priority
        if priority > oldPrioroty:
            MaxHeap.SiftUp(self, index)
        else: MaxHeap.SiftDown(index)
        
        

class MinHeap:
    def __init__(self, maxSize = 1, currentSize = 0):
        self.maxSize = maxSize
        self.currentSize = currentSize
        self.minHeapArray = [None] * maxSize
    
    
    def Parent(index):
        return (index - 1) // 2
    
    def LeftChild(index):
        return 1 + (index * 2)
    
    def RightChild(index):
        return 2 + (index * 2)
    
    def GetMin(self):
        return self.minHeapArray[0]
    
    def SiftUp(self, index):
        while index > 0 and self.minHeapArray[MinHeap.Parent(index)] > self.minHeapArray[index]:
            Swap(self.minHeapArray, self.minHeapArray[MinHeap.Parent(index)], self.minHeapArray[index])
            index = MinHeap.Parent(index)
    
    def SiftDown(self, index):
        maxIndex = index
        left = MinHeap.LeftChild(index)
        if left <= self.currentSize and self.minHeapArray[left] < self.minHeapArray[maxIndex]:
            maxIndex = left
        
        right = MinHeap.RightChild(index)
        if right <= self.currentSize and self.minHeapArray[right] < self.minHeapArray[maxIndex]:
            maxIndex = right
        
        if index != maxIndex:
            Swap(self.minHeapArray, self.minHeapArray[index], self.minHeapArray[maxIndex])
            MinHeap.SiftDown(self, maxIndex)
    
    def Insert(self, priority):
        if self.currentSize == self.maxSize:
            self.maxSize += 1
            self.minHeapArray.append(None)
        self.currentSize += 1
        self.minHeapArray[self.currentSize] = priority
        MinHeap.SiftUp(priority)
        
    def ExtractMin(self):
        result = self.minHeapArray[0]
        self.minHeapArray[0] = self.minHeapArray[self.currentSize]
        self.currentSize -= 1
        MinHeap.SiftDown(self, 0)
        return result
    
    def Remove(self, index):
        self.minHeapArray[index] = -infinity
        MinHeap.SiftUp(self, index)
        MinHeap.ExtractMin(self)
        
    def ChangePriority(self, index, priority):
        oldPrioroty = priority
        self.minHeapArray[index] = priority
        if priority < oldPrioroty:
            MinHeap.SiftUp(self, index)
        else: MinHeap.SiftDown(index)
    
    def BuildMinHeap(self, array):
        size = len(array) - 1
        for i in range(size // 2, -1, -1):
            MinHeap.SiftDown(i)