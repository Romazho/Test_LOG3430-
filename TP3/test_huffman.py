from collections import Counter
from functools import total_ordering
from huffman import Huffman
import unittest
import builtins
from unittest.mock import Mock
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

    # On test les valeurs indexées par data dans le codebook suite à un appel à la méthode build_codebook
    def test_build_codebook_it_should_correctly_assign_leaf_prefixes_according_to_Huffman_algorithm(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'ab', left, right)
        self.assertEqual(huffman.codebook[huffman.left.data], '0')
        self.assertEqual(huffman.codebook[huffman.right.data], '1')

    # On test la valeur de l'attribut data suite à un appel à la fonction from_string
    def test_from_string_it_should_assign_data_with_parameter(self):
        huffman = Huffman.from_string('cab')
        self.assertEqual(huffman.data, 'cab')

    # On test si data ('abc') a influencé la valeur de retour de la fonction encode_tree
    def test_encode_tree_it_should_assign_encoded_tree_to_1_and_append_data_when_is_leaf_is_true(self):
        huffman = Huffman(3, 'abc')
        self.assertEqual(huffman.encode_tree(), ('1', 'abc'))

    # On test la valeur de l'attribut data suite à un appel à la fonction unzip_tree
    def test_unzip_tree_it_should_assign_data_with_the_first_leaf_in_leaves(self):
        huffman = Huffman.unzip_tree('10', 'zyx', 0)
        self.assertEqual(huffman.data, 'z')

    # On test si la fonction huffman_decode utilise bien data pour decoder le string passé en paramètre
    def test_huffman_decode_it_should_use_data_to_return_the_decoded_string(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'ab', left, right)
        encoded = huffman.huffman_encode('ab')
        decoded = huffman.huffman_decode(encoded)
        self.assertEqual('ab', decoded)

    ########## Tests de la tranche left ##########

    # On test la valeur de l'attribut left avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_left_with_parameter(self):
        left = Huffman(2, 'def')
        huffmanWithLeft = Huffman(1, 'abc', left)
        huffmanNoLeft = Huffman(1, 'abc')
        self.assertEqual(huffmanWithLeft.left, left)
        self.assertIsNone(huffmanNoLeft.left)

    # On vérifie si la valeur de left ('a') est bien initialisé dans le codebook
    def test_build_codebook_it_should_initialize_data_of_left_in_codebook(self):
        left = Huffman(1, 'a')
        huffman = Huffman(2, 'ab', left)
        huffman.build_codebook()
        self.assertEqual(huffman.codebook['a'], '0')

    # On vérifie si la valeur de left ('a') est bien utilisé dans l'encodage
    def test_encode_tree_it_should_use_left_leaf_to_encode(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'Doesnt matter what it is', left, right)
        self.assertEqual(huffman.encode_tree(), ('011', 'ab'))

    # On vérifie si la valeur de left ('a') est bien utilisé dans l'encodage et ensuite dans le décodage
    def test_huffman_decode_it_should_use_left_leaf_to_decode(self):
        left = Huffman(1, 'a')
        huffman = Huffman(2, 'doesnt matter', left)
        encoded = huffman.huffman_encode('a')
        self.assertEqual(encoded[0], '0')
        decoded = huffman.huffman_decode(encoded)
        self.assertEqual('a', decoded)

    ########## Tests de la tranche right ##########

    # On test la valeur de l'attribut right avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_right_with_parameter(self):
        right = Huffman(2, 'def')
        huffmanWithRight = Huffman(1, 'abc', None, right)
        huffmanNoRight = Huffman(1, 'abc')
        self.assertEqual(huffmanWithRight.right, right)
        self.assertIsNone(huffmanNoRight.right)

    # On vérifie si la valeur de right ('b') est bien initialisé dans le codebook
    def test_build_codebook_it_should_initialize_data_of_right_in_codebook(self):
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'ab', None, right)
        huffman.build_codebook()
        self.assertEqual(huffman.codebook['b'], '1')

    # On vérifie si la valeur de right ('b') est bien utilisé dans l'encodage du string
    def test_encode_tree_it_should_use_right_leaf_to_encode(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'anything', left, right)
        self.assertEqual(huffman.encode_tree(), ('011', 'ab'))

    # On vérifie si la valeur de right ('b') est bien utilisé dans l'encodage et ensuite dans le décodage
    def test_huffman_decode_it_should_use_right_leaf_to_decode(self):
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'something', None, right)
        encoded = huffman.huffman_encode('b')
        self.assertEqual(encoded[0], '1')
        decoded = huffman.huffman_decode(encoded)
        self.assertEqual('b', decoded)

    ########## Tests de la tranche codebook ##########

    # On test la valeur de l'attribut codebook avec le constructeur de la classe Huffman
    def test_init_it_should_initialize_codebook(self):
        huffman = Huffman(1, 'abc')
        self.assertEqual(huffman.codebook, {})

    # On vérifie si les valeurs de left et de right sont bien initialisé dans le codebook
    def test_build_codebook_it_should_initialize_codebook_with_left_and_right_nodes(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'anything', left, right)
        self.assertEqual(huffman.codebook['a'], '0')
        self.assertEqual(huffman.codebook['b'], '1')

    # On vérifie si les valeurs dans le codebook sont utilisé dans l'encodage
    def test_huffman_encode_it_should_use_codebook_to_encode(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'anything once again', left, right)
        encoded = huffman.huffman_encode('ab')
        self.assertEqual(encoded, '01')
    
    ########## Tests pour la couverture maximale ##########
    
    # On vérifie que la représentation en string d'un noeud de Huffman est correcte
    def test_print_it_should_print_a_huffman_node_according_to_implementation(self):
        left = Huffman(1, 'a')
        right = Huffman(1, 'b')
        huffman = Huffman(2, 'abc', left, right)
        builtins.print = Mock()
        builtins.print(repr(huffman))
        builtins.print.assert_called_with('<Huffman(data: abc, left: a, right: b>')

    # On vérifie que huffman_decode soulève une exception ValueError si le code qui lui est passé est invalide
    def test_huffman_decode_it_should_raise_ValueError_when_code_is_invalid(self):
        with self.assertRaises(ValueError) as assertRaisesContext:
            huffman = Huffman(1, 'abc')
            huffman.huffman_decode('abcdefg')
        self.assertTrue('Error when encoding the string' in assertRaisesContext.exception.args)
    
    # On vérifie que unzip soulève une exception ValueError pour une string invalide
    def test_unzip_it_should_raise_ValueError_when_meta_string_is_of_length_5(self):
        with self.assertRaises(ValueError) as assertRaisesContext:
            Huffman.unzip('abcdefgh')
        self.assertTrue('Error when encoding the string' in assertRaisesContext.exception.args)
    
    # On vérifie que unzip_tree retourne None si l'index donné est placé au delà de la longueur de l'arbre encodé
    def test_unzip_tree_it_should_return_None_for_index_over_the_length_of_the_encoded_tree(self):
        encodedTreeDummy = 'abcdefg'
        dummyLeaf = Huffman(1, 'abc')
        index = len(encodedTreeDummy) + 1
        self.assertIsNone(Huffman.unzip_tree(encodedTreeDummy, [dummyLeaf], index))


if __name__ == '__main__':
    unittest.main()
