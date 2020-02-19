from BST import BST, node
import unittest


class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()
    #test boite noir###################################################################

    # cas où BST existe et node exist
    def test_delete_node_when_node_is_not_none(self):
        self.bst.insert(2)
        self.bst.delete_node(node(2))
        self.assertEqual(self.bst.find(2), None)
        self.assertEqual(self.bst.root, None)

    # cas où BST existe et node n'existe pas
    def test_delete_node_when_node_is_not_none_but_value_is_not_in_BST(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(node(100)), None)

    # cas où BST = None et node n'existe pas
    def test_delete_node_when_node_is_none_and_BST_is_none(self):
        self.bst.root = None
        self.assertEqual(self.bst.delete_node(node(100)), None)

    # impossible de tester ce cas
    # cas où BST = None et node existe
    def test_delete_node_when_node_is_not_none_and_BST_is_none(self):
        self.bst.root = None
        self.bst.insert(6)  # ici BST n'est plus "None" (vide)
        self.assertEqual(self.bst.delete_node(node(6)), None)

    # tests boite blanche###################################################################

    # cas où le noeud n'existe pas
    def test_delete_node_when_node_is_none_should_none(self):
        self.assertEqual(self.bst.delete_node(None), None)

    # cas où le search retourne False
    def test_delete_node_when_node_is_none_should_none(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(100), None)

    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_root(self):
        self.bst.insert(4)
        self.bst.delete_node(node(4))
        self.assertEqual(self.bst.root, None)

    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_left_leaf(self):
        self.bst.insert(4)
        self.bst.insert(2)
        node = self.bst.find(2)
        self.bst.delete_node(node)
        self.assertEqual(node.parent.left, None)

    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_right_leaf(self):
        self.bst.insert(4)
        self.bst.insert(5)
        node = self.bst.find(5)
        self.bst.delete_node(node)
        self.assertEqual(node.parent.right, None)

    # nbChild = 1 and child is left and is root
    def test_delete_node_when_the_node_to_delete_has_one_left_child_and_is_root(self):
        self.bst.insert(2)
        self.bst.insert(1)
        nodeToDelete = self.bst.find(2)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, nodeToDelete.left.value)

    # nbChild = 1 and child is right and is NOT root and node to delete is right to parent
    def test_delete_node_when_the_node_to_delete_has_one_right_child_and_is_not_root(self):
        self.bst.insert(5)
        self.bst.insert(8)
        self.bst.insert(7)
        nodeToDelete = self.bst.find(8)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.right.value, nodeToDelete.left.value)

    # nbChild = 1 and child is right and is NOT root and node to delete is left to parent
    def test_delete_node_when_the_node_to_delete_has_one_right_child_and_is_not_root(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(4)
        nodeToDelete = self.bst.find(3)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.left.value, nodeToDelete.right.value)

    # nbChild = 2 and child is right and is NOT root and node to delete is left to parent
    def test_delete_node_when_the_node_to_delete_has_two_children(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(8)
        self.bst.insert(7)
        self.bst.insert(10)
        nodeToDelete = self.bst.find(5)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, 7)

    # test #2 for 3 nodes
    def test_delete_node_when_the_node_to_delete_has_two_children(self):
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.insert(3)
        nodeToDelete = self.bst.find(5)
        rightNode = nodeToDelete.right
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, rightNode.value)


if __name__ == '__main__':
    unittest.main()
