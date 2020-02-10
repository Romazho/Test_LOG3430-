import unittest
from models import Contact

class TestContact(unittest.TestCase):
    def test_email(self):
        self.cont_1 = Contact('Noureddine', 'Kerzazi', 50000)
        self.cont_2 = Contact('Bram', 'Adam', 60000)

        self.assertEqual(self.cont_1.email, 'Noureddine.Kerzazi@polymtl.ca')
        self.assertEqual(self.cont_2.email, 'Bram.Adam@polymtl.ca')
        # Hypothèse: Ici, il y avait un typo: au lieu d'avoir first_name, il y avait juste first
        self.cont_1.first_name = 'Noureddine2'
        self.cont_2.first_name = 'Bram2'
        self.assertEqual(self.cont_1.email, 'Noureddine2.Kerzazi@polymtl.ca')
        self.assertEqual(self.cont_2.email, 'Bram2.Adam@polymtl.ca')

    def test_fullname(self):
        self.cont_1 = Contact('Noureddine', 'Kerzazi', 50000)
        self.cont_2 = Contact('Bram', 'Adam', 60000)

        self.assertEqual(self.cont_1.fullname, 'Noureddine Kerzazi')
        self.assertEqual(self.cont_2.fullname, 'Bram Adam')
        # Hypothèse: Ici, il y avait un typo: au lieu d'avoir first_name, il y avait juste first
        self.cont_1.first_name = 'Noureddine2'
        self.cont_2.first_name = 'Bram2'
        self.assertEqual(self.cont_1.fullname, 'Noureddine2 Kerzazi')
        self.assertEqual(self.cont_2.fullname, 'Bram2 Adam')
    
    def test_apply_raise(self):
        self.cont_1 = Contact('Noureddine', 'Kerzazi', 50000)
        self.cont_2 = Contact('Bram', 'Adam', 60000)
        self.cont_1.apply_raise()
        self.cont_2.apply_raise()
        self.assertEqual(self.cont_1.pay, 52500)
        self.assertEqual(self.cont_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()
