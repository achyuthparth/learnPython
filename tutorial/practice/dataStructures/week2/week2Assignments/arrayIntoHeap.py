from math import inf as infinity

'''convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap using
only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap instead
of a max-heap in this problem.'''

# python3

#swap alogrithm
''' 
swaps = []
def Swap(position1, position2):
    returnTuple = tuple((position1, position2))
    swaps.append(returnTuple)'''    
    
"""Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

class MinHeap:
    def __init__(self, maxSize = 1, currentSize = 0):
        self.maxSize = maxSize
        self.currentSize = currentSize
        self.minHeapArray = [None] * (self.maxSize)
    
    def Swap(heapArray, position1, position2):
        heapArray[position1], heapArray[position2] = heapArray[position2], heapArray[position1]
        return heapArray
    
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
            MinHeap.Swap(self.minHeapArray, self.minHeapArray[MinHeap.Parent(index)], self.minHeapArray[index])
            index = MinHeap.Parent(index)
    
    def SiftDown(self, index):
        maxIndex = index
        left = MinHeap.LeftChild(index)
        if left <= self.currentSize and self.minHeapArray[left] > self.minHeapArray[maxIndex]:
            maxIndex = left
        
        right = MinHeap.RightChild(index)
        if right <= self.currentSize and self.minHeapArray[right] < self.minHeapArray[maxIndex]:
            maxIndex = right
        
        if index != maxIndex:
            MinHeap.Swap(self.minHeapArray, self.minHeapArray[index], self.minHeapArray[maxIndex])
            MinHeap.SiftDown(self, maxIndex)
    
    def Insert(self, priority):
        self.minHeapArray[self.currentSize] = priority
        MinHeap.SiftUp(self, priority - 1)
        
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
    
    def BuildMinHeap(heapArray, arrayLength):
        heap = MinHeap(arrayLength, arrayLength - 1)
        for i in range(arrayLength):
            MinHeap.Insert(heap, priority = heapArray[i])
        for index in range(arrayLength, -1, -1):
            heap[index] = MinHeap.ExtractMin(heap)
        return heap.minHeapArray
        '''
def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    MinHeap.BuildMinHeap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

'''