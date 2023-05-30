from binaryTree import Tree #as binaryTree
from binaryTree import Node #as BinaryTreeNode
import unittest

class TestBinaryTree(unittest.TestCase):
    
    def testHeight(self):
        sampleTree = Tree()
        sampleTree.setRoot(Node("animal"))
        Node.setRight(sampleTree.getRoot(), Node("insect"))
        Node.setLeft(sampleTree.getRoot(), Node("reptile"))
        height = Tree.height(sampleTree)
        self.assertEqual(height, 2)
        #works
        
    def testSize(self):
        
        sampleTree = Tree()
        sampleTree.setRoot(Node("animal"))
        Node.setRight(sampleTree.getRoot(), Node("insect"))
        Node.setLeft(sampleTree.getRoot(), Node("reptile"))
        size = Tree.size(sampleTree)
        self.assertEqual(size, 3)
        #works
        
    def testInOrderTraversal(self):
        sampleTree = Tree()
        sampleTree.setRoot(Node("animal"))
        Node.setRight(sampleTree.getRoot(), Node("insect"))
        Node.setLeft(sampleTree.getRoot(), Node("reptile"))
        Tree.callDfsInOrderTraversal(sampleTree)
        #works
    
    def testPreOrderTraversal(self):
        sampleTree = Tree()
        sampleTree.setRoot(Node("animal"))
        Node.setRight(sampleTree.getRoot(), Node("insect"))
        Node.setLeft(sampleTree.getRoot(), Node("reptile"))
        Tree.callPreOrderTraversal(sampleTree)
        #works
        
    def testPostOrderTraversal(self):
        sampleTree = Tree()
        sampleTree.setRoot(Node("animal"))
        Node.setRight(sampleTree.getRoot(), Node("insect"))
        Node.setLeft(sampleTree.getRoot(), Node("reptile"))
        Tree.callPostOrderTraversal(sampleTree)
        #works
        
    def testBFS(self):
        sampleTree = Tree()
        sampleTree.setRoot(Node(6))
        Node.setRight(sampleTree.getRoot(), Node(3))
        Node.setLeft(sampleTree.getRoot(), Node(2))
        Tree.callBFS(sampleTree)
        #works
    
if __name__ == '__main__':
    unittest.main()    
