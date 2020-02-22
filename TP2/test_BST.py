from BST import BST, node
import unittest


class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()

    # tests boite noire ###################################################################

    # cas où BST = None et node n'existe pas (B1N1)
    def test_delete_node_when_node_is_none_and_BST_is_none(self):
        self.bst.root = None
        self.assertEqual(self.bst.delete_node(node(100)), None)

    # impossible de tester ce cas
    # cas où BST = None et node existe (B1N2)
    def test_delete_node_when_node_is_not_none_and_BST_is_none(self):
        self.bst.root = None
        self.bst.insert(6)  # ici BST n'est plus "None" (vide)
        self.assertEqual(self.bst.delete_node(node(6)), None)

    # cas où BST existe et node n'existe pas (B2N1)
    def test_delete_node_when_node_is_not_none_but_value_is_not_in_BST(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(node(100)), None)

    # cas où BST existe et node exist (B2N2)
    def test_delete_node_when_node_is_not_none(self):
        self.bst.insert(2)
        self.bst.delete_node(node(2))
        self.assertEqual(self.bst.find(2), None)
        self.assertEqual(self.bst.root, None)

    # tests boite blanche ###################################################################

    #note: nbChild indique le nombre d'enfant que le node contient

    # cas où le noeud n'existe pas (node == None)
    def test_delete_node_when_node_is_none_it_should_return_none(self):
        self.assertEqual(self.bst.delete_node(None), None)

    # cas où le search retourne False (self.search(node.value) == False)
    def test_delete_node_when_node_is_not_in_BST_it_should_return_none(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.delete_node(node(100)), None)

    # cas où nbChild = 0 et le node à delete est la racine 
    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_root(self):
        self.bst.insert(4)
        self.bst.delete_node(node(4))
        self.assertEqual(self.bst.root, None)

    # cas où nbChild = 0 et le node est un enfant gauche de la racine
    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_left_leaf(self):
        self.bst.insert(4)
        self.bst.insert(1)
        node = self.bst.find(1)
        self.bst.delete_node(node)
        self.assertEqual(node.parent.left, None)

    # cas où nbChild = 0 et le node est un enfant à droite de la racine
    def test_delete_node_when_the_node_to_delete_has_no_children_and_is_right_leaf(self):
        self.bst.insert(4)
        self.bst.insert(10)
        node = self.bst.find(10)
        self.bst.delete_node(node)
        self.assertEqual(node.parent.right, None)

    # cas où nbChild = 1, son fils est à sa gauche et le noeud est la racine
    def test_delete_node_when_the_node_to_delete_has_one_left_child_and_is_root(self):
        self.bst.insert(5)
        self.bst.insert(1)
        nodeToDelete = self.bst.find(5)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, nodeToDelete.left.value)

    # cas où nbChild = 1, son fils est à sa gauche, le noeud n'est pas la racine et le noeud est à droite de son parent
    def test_delete_node_when_the_node_to_delete_has_one_left_child_and_is_not_root(self):
        self.bst.insert(5)
        self.bst.insert(8)
        self.bst.insert(7)
        nodeToDelete = self.bst.find(8)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.right.value, nodeToDelete.left.value)

    # cas où nbChild = 1, son fils est à sa droite, le noeud n'est pas la racine et le noeud est à gauche de son parent
    def test_delete_node_when_the_node_to_delete_has_one_right_child_and_is_not_root(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(4)
        nodeToDelete = self.bst.find(3)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.left.value, nodeToDelete.right.value)

    # cas où nbChild = 2, on vérifie si l'enfant de droite devient la racine
    def test_delete_node_when_the_node_to_delete_has_two_children(self):
        self.bst.insert(5)
        self.bst.insert(6)
        self.bst.insert(3)
        nodeToDelete = self.bst.find(5)
        rightNode = nodeToDelete.right
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, rightNode.value)

    # cas où nbChild = 2, on vérifie si le noeud le plus petit de la partie droite de l'arbre devient la racine 
    def test_delete_node_when_the_node_to_delete_has_two_children_and_root_is_the_smallest_child_from_the_right_branch(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(8)
        self.bst.insert(7)
        self.bst.insert(10)
        nodeToDelete = self.bst.find(5)
        self.bst.delete_node(nodeToDelete)
        self.assertEqual(self.bst.root.value, 7)

if __name__ == '__main__':
    unittest.main()
