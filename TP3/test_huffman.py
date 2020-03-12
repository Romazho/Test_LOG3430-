from collections import Counter
from functools import total_ordering
from huffman import Huffman
import unittest
import heapq


class TestBST(unittest.TestCase):

    def setUp(self):
        self.huffman = Huffman(0, 'testing')

    ################ tests pour l'attribut weight ################

    # On vérifie si l'initialisation de la variable weight s'est assigné correctement
    def test_init_it_should_initialise_weight(self):
        self.assertEqual(self.huffman.weight, 0)
        self.assertEqual(self.huffman.left, None)  # à changer de place
        self.assertEqual(self.huffman.right, None)  # à changer de place
        self.assertEqual(self.huffman.codebook, {})  # à changer de place

    # On vérifie si l'asignation de l'attribut de weight s'est asiigné corrctement
    def test_from_string_it_should_assign_weight_according_to_huffman_algorithm(self):
        huff2 = Huffman.from_string("testing")
        self.assertEqual(huff2.weight, len("testing"))

    ################ tests pour l'attribut data ################

    # On vérifie si l'initialisation de la variable data s'est assigné correctement
    def test_init_it_should_initialise_data(self):
        self.assertEqual(self.huffman.data, 'testing')

    # On vérifie que le data n'a pas été changé
    def test_build_codebook_it_should(self):
        self.huffman.build_codebook()
        self.assertEqual(self.huffman.data, 'testing')


if __name__ == '__main__':
    unittest.main()
