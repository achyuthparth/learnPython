import copy


class LinkedList:
    def __init__(self):
        self.head = None
        
    def getHead(self):
        return self.head
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        if self.isEmpty is True:
            return 0
        currentNode = self.head
        count = 1
        while LinkedListNode.getNext(currentNode) != None:
            count += 1
            currentNode = LinkedListNode.getNext(currentNode)
        return count
    
    def pushNodeFront(self, newNode):
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode
        
    def pushValueFront(self, value):
        newNode = LinkedListNode(value)
#no elements in linked list, at least 1 element in Linked List
        self.pushNodeFront(newNode)
        return newNode
    
    def printLinkedList(self):
        currentNode = self.head
        while currentNode != None:
            print(LinkedListNode.getValue(currentNode))
            currentNode = LinkedListNode.getNext(currentNode)

        
    def pushNodeBack(self, newNode):
#no elements in linked list, at least 1 element in linked list
#if using a tail, set tail to the new back node
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode != None:
                
                if LinkedListNode.getNext(currentNode) is None:
                    LinkedListNode.setNext(currentNode, newNode)
                    break
                else:
                    currentNode = LinkedListNode.getNext(currentNode)
    
    def pushValueBack(self, value):
        newNode = LinkedListNode(value)
        self.pushNodeBack(newNode)
        return newNode
    
    def booleanFindValue(self, searchValue):
        if self.isEmpty() is True:
            return False
        currentNode = self.head
        while currentNode != None:
            if LinkedListNode.getValue(currentNode) == searchValue:
                return True
            currentNode = LinkedListNode.getNext(currentNode)
        return False
        
    def popFrontNode(self):
        if self.isEmpty() is True:
            return None
        oldHead = copy.deepcopy(self.head)
        newHead = LinkedListNode.getNext(oldHead)
        self.head = newHead
        return oldHead
        
    def popFrontValue(self):
        node = LinkedList.popFrontNode(self)
        return LinkedListNode.getValue(node)
        
    def popBack(self):
        if self.isEmpty() is True:
            return None
        currentNode = self.head
        print("head is: " + str(LinkedListNode.getValue(self.head)))
        if LinkedListNode.getNext(currentNode) is None:
            returnNode = currentNode
            self.head = None
            return returnNode
        while LinkedListNode.getNext(currentNode) != None:
            print("current node is: " + str(LinkedListNode.getValue(currentNode)))
            nextNode = LinkedListNode.getNext(currentNode)
            if LinkedListNode.getNext(nextNode) is None:
                returnNode = LinkedListNode.getNext(currentNode)
                LinkedListNode.setNext(currentNode, None)
                return returnNode
            currentNode = LinkedListNode.getNext(currentNode)
    
    def findFirstValue(self, value):
        if self.isEmpty() == True:
            return None
        currentNode = self.head
        while LinkedListNode.getNext(currentNode) != None:
            nextNode = LinkedListNode.getNext(currentNode)
            if LinkedListNode.getValue(nextNode) is value:
                return nextNode
        return None
    
    def popFirstValue(self, value):
        if self.isEmpty() == True:
            return None
        currentNode = self.head
        while LinkedListNode.getNext(currentNode) != None:
            nextNode = LinkedListNode.getNext(currentNode)
            if LinkedListNode.getValue(nextNode) is value:
                LinkedListNode.setNext(currentNode, LinkedListNode.getNext(nextNode))
                return nextNode
        return None
    
    def addBeforeValue(self, value, before):
        newNode = LinkedListNode(value)
        currentNode = self.head
        while LinkedListNode.getNext(currentNode) != None:
            nextNode = LinkedListNode.getNext(currentNode)
            if LinkedListNode.getValue(nextNode) is before:
                LinkedListNode.setNext(currentNode, newNode)
                LinkedListNode.setNext(newNode, nextNode)
                break
            
class LinkedListNode:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    