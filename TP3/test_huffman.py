from collections import Counter
from functools import total_ordering
from huffman import Huffman
import unittest
import heapq


class TestBST(unittest.TestCase):

    def setUp(self):
        pass

    ################ 1. Tester les rapporteurs (il n'y a pas de "R") ################

    ################ 2. Tester les constructeurs ################

    # Je ne sais pas si on peut tester plusieurs attributs dans une seule méthode

    # On vérifie si l'initialisation des variables
    def test_init_it_should_initialise_all_attributes(self):
        self.huffman = Huffman(0, '1', None, None)
        self.assertEqual(self.huffman.weight, 0)
        self.assertEqual(self.huffman.data, '1')
        self.assertEqual(self.huffman.left, None)
        self.assertEqual(self.huffman.right, None)
        self.assertEqual(self.huffman.codebook, {})

    ################ 3. Tester les transformateurs ################

    def test_build_codebook_it_should(self):
        pass

    ################ 4. Tester les autres ################


if __name__ == '__main__':
    unittest.main()
