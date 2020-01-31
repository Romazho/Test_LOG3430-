import unittest
import calcul
# Voir les assertions possibles ici
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCalc(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(calcul.somme(18, 2), 20)
        self.assertEqual(calcul.somme(-1, 1), 0)
        self.assertEqual(calcul.somme(-1, -1), -2)
    def test_soustraire(self):
        self.assertEqual(calcul.soustraire(18, 2), 16)
        self.assertEqual(calcul.soustraire(-1, 1), -2)
        self.assertEqual(calcul.soustraire(-1, -1), 0)
    def test_multiplier(self):
        self.assertEqual(calcul.multiplier(18, 2), 36)
        self.assertEqual(calcul.multiplier(-1, 1), -1)
        self.assertEqual(calcul.multiplier(-1, -1), 1)
    def test_diviser(self):
        self.assertEqual(calcul.diviser(18, 2), 9)
        self.assertEqual(calcul.diviser(-1, 1), -1)
        self.assertEqual(calcul.diviser(-1, -1), 1)
        self.assertEqual(calcul.diviser(18, 5), 3.6)

        #self.assertRaises(ValueError, calcul.diviser, 20, 0)

        with self.assertRaises(ValueError):
            calcul.diviser(20, 0)

if __name__ == '__main__':
    unittest.main()




