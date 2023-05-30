from linkedList import LinkedList
from linkedList import Node as LinkedListNode
import unittest
class TestLinkedList(unittest.TestCase):
    
    def testPushValueFront(self):
        sampleList = LinkedList()
        testNode = sampleList.pushValueFront(7)
        evalNode = LinkedListNode(7)
        testNodeValue = LinkedListNode.getValue(testNode)
        evalNodeValue = LinkedListNode.getValue(evalNode)
        self.assertEqual(testNodeValue, evalNodeValue)
        #works
        

    def testPushValueBack(self):
        sampleList = LinkedList()
        testNode = sampleList.pushValueFront(7)
        LinkedList.printLinkedList(sampleList) #works
        testNodeValue = LinkedListNode.getValue(testNode)
        evalNode = LinkedListNode(7)
        evalNodeValue = LinkedListNode.getValue(evalNode)
        testNode2 = sampleList.pushValueBack(9)
        LinkedList.printLinkedList(sampleList)
        evalNode2 = LinkedListNode(9)
        testNode2Value = LinkedListNode.getValue(testNode2)
        evalNodeValue2 = LinkedListNode.getValue(evalNode2)
        self.assertEqual(testNodeValue, evalNodeValue)
        self.assertEqual(testNode2Value, evalNodeValue2)
        #works

    def testIsEmpty(self):
        sampleList = LinkedList()
        self.assertEqual(LinkedList.isEmpty(sampleList), True)
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        self.assertEqual(LinkedList.isEmpty(sampleList), False)
        #works 

    def testBooleanFindValue(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        search10 = sampleList.booleanFindValue(10)
        search11 = sampleList.booleanFindValue(11)
        self.assertEqual(search10, False)
        self.assertEqual(search11, True)
        #works
    
    def testPopFront(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        pop = LinkedList.popFrontNode(sampleList)
        sampleList.printLinkedList()
        popVal = LinkedListNode.getValue(pop)
        self.assertEqual(popVal, 11)
        #works
        
    def testPopBack(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        pop = LinkedList.popBack(sampleList)
        sampleList.printLinkedList()
        popVal = LinkedListNode.getValue(pop)
        self.assertEqual(popVal, 7)
        #works
        
    def testFindFirstValue(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        testNode = LinkedList.findFirstValue(sampleList, 9)
        testNodeValue = LinkedListNode.getValue(testNode)
        self.assertEqual(testNodeValue, 9)
        #works
        
    
    def testPopFirstValue(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        testNode = LinkedList.popFirstValue(sampleList, 9)
        testNodeValue = LinkedListNode.getValue(testNode)
        self.assertEqual(testNodeValue, 9)
        #works

    def testSize(self):
        sampleList = LinkedList()
        sampleList.pushValueFront(7)
        sampleList.pushValueFront(9)
        sampleList.pushValueFront(11)
        sampleList.printLinkedList()
        sizeTest = LinkedList.size(sampleList)
        self.assertEqual(sizeTest, 3)
        #works

if __name__ == '__main__':
    unittest.main()    
