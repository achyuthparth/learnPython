class naryTree:
    
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def setRoot(self, rootNode):
        self.root = rootNode
        
    def nodeHeight(root):
        if naryTreeNode.getChildList(root) == []:
            return 1
        
        return 1 + max(naryTree.nodeHeight(child) for child in naryTreeNode.getChildList(root))
        
    def height(self):
        return naryTree.nodeHeight(naryTree.getRoot(self))
    
    
class naryTreeNode:
    def __init__(self, value = None, childList=None):
        if childList is None:
            childList = []
        self.value = value
        self.childList = childList
        
    def getChildList(self):
        return self.childList
    
    def addChildNode(self, newChild):
        naryTreeNode.getChildList(self).append(newChild)
        
    def addChildValue(self, newChildValue):
        newChild = naryTreeNode(newChildValue)
        naryTreeNode.addChildNode(self, newChild)
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        