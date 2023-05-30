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
        while Node.getNext(currentNode) != None:
            count += 1
            currentNode = Node.getNext(currentNode)
        return count
    
    def pushNodeFront(self, newNode):
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode
        
    def pushValueFront(self, value):
        newNode = Node(value)
#no elements in linked list, at least 1 element in Linked List
        self.pushNodeFront(newNode)
        return newNode
    
    def printLinkedList(self):
        currentNode = self.head
        while currentNode != None:
            print(Node.getValue(currentNode))
            currentNode = Node.getNext(currentNode)

        
    def pushNodeBack(self, newNode):
#no elements in linked list, at least 1 element in linked list
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode != None:
                
                if Node.getNext(currentNode) is None:
                    Node.setNext(currentNode, newNode)
                    break
                else:
                    currentNode = Node.getNext(currentNode)
    
    def pushValueBack(self, value):
        newNode = Node(value)
        self.pushNodeBack(newNode)
        return newNode
    
    def booleanFindValue(self, searchValue):
        if self.isEmpty() is True:
            return False
        currentNode = self.head
        while currentNode != None:
            if Node.getValue(currentNode) == searchValue:
                return True
            currentNode = Node.getNext(currentNode)
        return False
        
    def popFrontNode(self):
        if self.isEmpty() is True:
            return None
        oldHead = copy.deepcopy(self.head)
        newHead = Node.getNext(oldHead)
        self.head = newHead
        return oldHead
        
    def popFrontValue(self):
        node = LinkedList.popFrontNode(self)
        return Node.getValue(node)
        
    def popBack(self):
        if self.isEmpty() is True:
            return None
        currentNode = self.head
        print("head is: " + str(Node.getValue(self.head)))
        if Node.getNext(currentNode) is None:
            returnNode = currentNode
            self.head = None
            return returnNode
        while Node.getNext(currentNode) != None:
            print("current node is: " + str(Node.getValue(currentNode)))
            nextNode = Node.getNext(currentNode)
            if Node.getNext(nextNode) is None:
                returnNode = Node.getNext(currentNode)
                Node.setNext(currentNode, None)
                return returnNode
            currentNode = Node.getNext(currentNode)
    
    def findFirstValue(self, value):
        if self.isEmpty() == True:
            return None
        currentNode = self.head
        while Node.getNext(currentNode) != None:
            nextNode = Node.getNext(currentNode)
            if Node.getValue(nextNode) is value:
                return nextNode
        return None
    
    def popFirstValue(self, value):
        if self.isEmpty() == True:
            return None
        currentNode = self.head
        while Node.getNext(currentNode) != None:
            nextNode = Node.getNext(currentNode)
            if Node.getValue(nextNode) is value:
                Node.setNext(currentNode, Node.getNext(nextNode))
                return nextNode
        return None
    
    def addBeforeValue(self, value, before):
        newNode = Node(value)
        currentNode = self.head
        while Node.getNext(currentNode) != None:
            nextNode = Node.getNext(currentNode)
            if Node.getValue(nextNode) is before:
                Node.setNext(currentNode, newNode)
                Node.setNext(newNode, nextNode)
                break
            
class Node:

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
    
    