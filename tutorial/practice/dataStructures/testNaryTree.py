from nArrayTree import naryTree as nArayTree
from nArrayTree import naryTreeNode as treeNode
import unittest

class testNArrayTree(unittest.TestCase):
    def testAddingChildren(self):
        testTree = nArayTree()
        testRoot = treeNode(4)
        nArayTree.setRoot(testTree, testRoot)
        treeNode.addChildValue(testRoot, 4)
        self.assertEqual(treeNode.getValue(treeNode.getChildList(nArayTree.getRoot(testTree))[0]), 4)
        #works

    def testHeight(self):
        testTree = nArayTree()
        testRoot = treeNode(4)
        nArayTree.setRoot(testTree, testRoot)
        treeNode.addChildValue(testRoot, 5)
        height = nArayTree.height(testTree)
        self.assertEqual(height, 2)
        treeNode.addChildValue(testRoot, 6)
        treeNode.addChildValue(treeNode.getChildList(testRoot)[1], 7)
        height2 = nArayTree.height(testTree)
        self.assertEqual(height2, 3)

if __name__ == '__main__':
    unittest.main()    
