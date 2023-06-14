import unittest
import arrayIntoHeap

class Test(unittest.TestCase):
    
    def testPriorityQueue(self):
        length = 5
        data = [5, 4, 3, 2, 1]
        test = arrayIntoHeap.MinHeap.BuildMinHeap(data, length)
        eval = [1, 2, 3, 4, 5]
        self.assertEqual(test, eval)
    
    
    #def testSwap
    
    #def testFromFile


    
if __name__ == '__main__':
    unittest.main()    