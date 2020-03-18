from collections import Counter
from functools import total_ordering
from huffman import Huffman
import unittest
import heapq


class TestHuffman(unittest.TestCase):
    ########## Tests de la tranche weight ##########

    # On test l'initialisation de l'attribut weight avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_weight_with_parameter(self):
        huffman = Huffman(1, 'abc')
        self.assertEqual(huffman.weight, 1)
    
    # On test la valeur de l'attribut weight suite à un appel à la fonction from_string
    def test_from_string_it_should_assign_length_of_string_to_weight_of_heap_head(self):
        huffman = Huffman.from_string('abbcccddddeeeee')
        self.assertEqual(huffman.weight, len('abbcccddddeeeee'))
    
    ########## Tests de la tranche data ##########

    # On test l'initialisation de l'attribut data avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_data_with_parameter(self):
        huffman = Huffman(1, 'abc')
        self.assertEqual(huffman.data, 'abc')
    
    # On test la valeur de l'attribut data suite à un appel à la fonction from_string
    def test_from_string_it_should_assign_data_with_parameter(self):
        huffman = Huffman.from_string('cab')
        self.assertEqual(huffman.data, 'cab')
    
    # On test les valeurs indexées par data dans le codebook suite à un appel à la méthode build_codebook
    def test_build_codebook_it_should_correctly_assign_leaf_prefixes_according_to_Huffman_algorithm(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'ab', left, right)
        self.assertEqual(huffman.codebook[huffman.left.data], '0')
        self.assertEqual(huffman.codebook[huffman.right.data], '1')
    
    ########## Tests de la tranche left ##########

    # On test la valeur de l'attribut left avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_left_with_parameter(self):
        left = Huffman(2, 'def')
        huffmanWithLeft = Huffman(1, 'abc', left)
        huffmanNoLeft = Huffman(1, 'abc')
        self.assertEqual(huffmanWithLeft.left, left)
        self.assertIsNone(huffmanNoLeft.left)
    

    ########## Tests de la tranche right ##########

    # On test la valeur de l'attribut right avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_right_with_parameter(self):
        right = Huffman(2, 'def')
        huffmanWithRight = Huffman(1, 'abc', None, right)
        huffmanNoRight = Huffman(1, 'abc')
        self.assertEqual(huffmanWithRight.right, right)
        self.assertIsNone(huffmanNoRight.right)
    
    ########## Tests de la tranche codebook ##########

    # On test la valeur de l'attribut codebook avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_codebook(self):
        huffman = Huffman(1, 'abc')
        self.assertEqual(huffman.codebook, {})
        
if __name__ == '__main__':
    unittest.main()