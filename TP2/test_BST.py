from BST import BST, node
import unittest


class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()

    # ca où on delete None
    def test_delete_node_when_node_to_delete_is_none(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(None), None)

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


if __name__ == '__main__':
    unittest.main()
