from BST import BST, node
import unittest

class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()

    
    def test_delete_node_when_node_is_none(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(None), None)

    def test_delete_node_when_node_is_not_none(self):
        self.bst.insert(2)
        self.bst.delete_node(node(2))
        self.assertEqual(self.bst.find(2), None)

if __name__ == '__main__':
    unittest.main()