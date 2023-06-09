from customQueue import Queue

class Tree:
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
    
    def setRoot(self, node):
        self.root = node
    
    def nodeHeight(root):
        if (root is None):
            return 0
        
        return 1 + max(Tree.nodeHeight(root.left), Tree.nodeHeight(root.right))
    
    def height(self):
        return Tree.nodeHeight(self.getRoot())

    def nodeSize(root):
        if root is None:
            return 0
        return 1 + Tree.nodeSize(root.left) + Tree.nodeSize(root.right)
    
    def size(self):
        if self.getRoot() is None:
            return 0
        return Tree.nodeSize(self.getRoot())

    #solve in order traversal recursively using the program stack
    def inOrderTraversal(root):
        if root is None:
            return
        Tree.inOrderTraversal(root.left)
        print(Node.getValue(root))
        Tree.inOrderTraversal(root.right)
    def callDfsInOrderTraversal(self):
        return Tree.inOrderTraversal(Tree.getRoot(self))
        
    def preOrderTraversal(root):
        if root is None:
            return
        print(Node.getValue(root))
        Tree.preOrderTraversal(root.left)
        Tree.preOrderTraversal(root.right)
    
    def callPreOrderTraversal(self):
        return Tree.preOrderTraversal(self.getRoot())
    
    def postOrderTraversal(root):
        if root is None:
            return
        Tree.postOrderTraversal(root.left)
        Tree.postOrderTraversal(root.right)
        print(Node.getValue(root))
        
    def callPostOrderTraversal(self):
        return Tree.postOrderTraversal(self.getRoot())
    
    def bfs(root):
        if root is None:
            return
        q = Queue()
        Queue.enqueue(q, root)
        while Queue.size(q) != 0:
            node = Queue.dequeue(q)
            print(Node.getValue(node))
            if Node.left(node) != None:
                Queue.enqueue(q, Node.left(node))
            if Node.right(node) != None:
                Queue.enqueue(q, Node.right(node))
    
    def callBFS(self):
        return Tree.bfs(self.getRoot())
'''        
    def dfspreOrderTraversal(self)
    
    def dfspostOrderTraversal(self)
    
    def bfsLevelTraversal(self)
'''

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
        
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
        
    def setLeft(self, leftNode):
        self.left = leftNode
    
    def left(self):
        return self.left

    def setRight(self, rightNode):
        self.right = rightNode
    
    def right(self):
        return self.right