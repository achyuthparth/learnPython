# python3

import sys
import threading



def compute_height(n, parents):
    nodeList = []
    sampleTree = NaryTree()
    for i in range(n):
        newNode = NaryTreeNode(i)
        nodeList.append(newNode)
    for j in range (len(parents)):
        if parents[j] == -1:
            NaryTree.setRoot(sampleTree, nodeList[j])
        else:
            NaryTreeNode.addChildNode(nodeList[parents[j]], nodeList[j])
    return NaryTree.height(sampleTree)
        


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()



class NaryTree:
    
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def setRoot(self, rootNode):
        self.root = rootNode
        
    def nodeHeight(root):
        if NaryTreeNode.getChildList(root) == []:
            return 1
        
        return 1 + max(NaryTree.nodeHeight(child) for child in NaryTreeNode.getChildList(root))
        
    def height(self):
        return NaryTree.nodeHeight(NaryTree.getRoot(self))
    
    
class NaryTreeNode:
    def __init__(self, value = None, childList=None):
        if childList is None:
            childList = []
        self.value = value
        self.childList = childList
        
    def getChildList(self):
        return self.childList
    
    def addChildNode(self, newChild):
        NaryTreeNode.getChildList(self).append(newChild)
        
    def addChildValue(self, newChildValue):
        newChild = NaryTreeNode(newChildValue)
        NaryTreeNode.addChildNode(self, newChild)
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        