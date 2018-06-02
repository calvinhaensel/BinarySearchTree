
from binarytreevis import *
import unittest

class Asg3Tests(unittest.TestCase):
    def test_binsearchtree_constructor1(self):
        bt1 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] )
        bt2 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] ) 
        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )

    def test_binsearchtree_inorder1(self):
        bt = BinarySearchTree(contents=[0, -1, 1]) 
        self.assertListEqual(bt.inorder(), [-1, 0, 1]) 
    
    def test_binsearchtree_preorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [2, 0, 1], bt.preorder() )
        
    def test_binsearchtree_postorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [1, 0, 2], bt.postorder() ) 
        
    def test_binsearchtree_levelorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1, 6, 10] ) 
        self.assertListEqual( [2, 0, 6, 1, 10], bt.levelorder() )  
        
    def test_binsearchtree_insert1(self):
        bt = BinarySearchTree() 
        bt.insert(0); bt.insert(-1); bt.insert(1)
        self.assertListEqual(bt.inorder(), [-1, 0, 1]) 
        bt1 = BinarySearchTree()
        bt1.insert(1000); bt1.insert(50); bt1.insert(2000); bt1.insert(1500);bt1.insert(3000);bt1.insert(1501);bt1.insert(1502)
        self.assertListEqual(bt1.inorder(), [50, 1000, 1500, 1501, 1502, 2000, 3000]) 
        bt1.insert(30)
        self.assertListEqual(bt1.inorder(), [30, 50, 1000, 1500, 1501, 1502, 2000, 3000])
        
    def test_binsearchtree_delete1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        bt.delete(0)
        bt1 = BinarySearchTree()
        bt1.insert(1000); bt1.insert(50); bt1.insert(2000); bt1.insert(1500);bt1.insert(3000);bt1.insert(1501);bt1.insert(1502)
        bt1.delete(1502)
        self.assertListEqual(bt.inorder(), [1, 2])
        self.assertListEqual(bt1.inorder(), [50, 1000, 1500, 1501, 2000, 3000])
        
    def test_binsearchtree_contains1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        self.assertTrue(0 in bt)    
        bt.delete(0)
        self.assertFalse(0 in bt)
        bt1 = BinarySearchTree()
        bt1.insert(1000); bt1.insert(50); bt1.insert(2000); bt1.insert(1500);bt1.insert(3000);bt1.insert(1501);bt1.insert(1502)
        self.assertTrue(1502.0 in bt1)
        self.assertFalse(0 in bt1)
    
if __name__ == '__main__':
    unittest.main()


