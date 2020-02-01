import sqlite3
import unittest.mock
import os
from DAOs import ContactDAO
from models import Contact

# To complete...
class TestContactDAO(unittest.TestCase):

    def setUp(self):
        self.db_file = 'temp.db'
        self.contactDAO = ContactDAO(self.db_file)
        self.contactDAO.init_db()
        self.contact1 = Contact(6, "R", "Z", "514999666", "Hakim@gmail.com", True, 20.3)
        self.contact2 = Contact(50, "H", "P", "514999666", "Hakim@gmail.com", False, 20.3)

    def tearDown(self):
        os.remove(self.db_file)
    
    def printContact(self, contactToPrint):
        if contactToPrint is None:
            print("Contact is None. Cannot print")
        else:
            print(contactToPrint.first_name)
            print(contactToPrint.last_name)
            print(contactToPrint.phone)
            print(contactToPrint.mail)
            print(contactToPrint.updated)
            print(contactToPrint.updated_date)
            print(contactToPrint)
    
    def areContactAttribsEqual(self, contact1 = None, contact2 = None):
        if contact1 is None:
            print("First contact is None (see first parameter)")
            return
        if contact2 is None:
            print("Second contact is None (see second parameter)")
            return
        self.assertEqual(contact1.first_name, contact2.first_name, "{0} not equal to {1}".format(self.contact1.first_name, self.contact2.first_name))
        self.assertEqual(contact1.last_name, contact2.last_name, "{0} not equal to {1}".format(self.contact1.last_name, self.contact2.last_name))
        self.assertEqual(contact1.phone, contact2.phone, "{0} not equal to {1}".format(self.contact1.phone, self.contact2.phone))
        self.assertEqual(contact1.mail, contact2.mail, "{0} not equal to {1}".format(self.contact1.mail, self.contact2.mail))
        self.assertEqual(contact1.updated, contact2.updated, "{0} not equal to {1}".format(self.contact1.updated, self.contact2.updated))
        self.assertEqual(contact1.updated_date, contact2.updated_date, "{0} not equal to {1}".format(self.contact1.updated_date, self.contact2.updated_date))
    
    def test_when_init_db_is_called_it_should_create_table(self):
        try:
            with sqlite3.connect(self.db_file) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM contact')
        except sqlite3.OperationalError:
            self.fail("Should not have raised sqlite3.OperationalError")
    
    #On vérifie que le nombre d'appel concorde avec la valeur de lastrowid
    def test_when_add_is_called_it_should_return_an_autoincremented_id(self):
        assert self.contactDAO.add(self.contact1) == 1, "should be 1"
        assert self.contactDAO.add(self.contact1) == 2, "should be 2"
        self.contactDAO.add(self.contact1)
        assert self.contactDAO.add(self.contact1) == 4, "should be 4"
    
    #On vérifie que contact1 à bel et bien été ajouté
    def test_get_by_id_after_add_should_return_inserted_value(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_id(1)
        self.areContactAttribsEqual(newContact, self.contact1)
    
    def test_get_by_names_after_add_should_return_inserted_value(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_names(self.contact1.first_name, self.contact1.last_name)
        self.areContactAttribsEqual(newContact, self.contact1)

    def test_get_by_id_with_undefined_rowid_should_return_None(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_id(2)
        self.assertIsNone(newContact)
    
    def test_get_by_names_with_notexisted_contact_should_return_None(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_names(self.contact2.first_name, self.contact2.last_name)
        self.assertIsNone(newContact)
    
    #Verifier que Contact.updated est assigne a False suite a l'appel de deactivate sur un contact avec updated = True dans la BD
    def test_deactivate_contact_then_get_it_with_id_should_be_not_updated(self):
        ctod = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctod)
        self.contactDAO.deactivate(1)
        res = self.contactDAO.get_by_id(1)
        self.assertFalse(res.updated)
    
    def test_deactivate_contact_on_undefined_id_should_return_zero(self):
        res = self.contactDAO.deactivate(1)
        self.assertEqual(res, 0, "deactivate did not return 0 on invalid id")
    
    def test_after_deleting_contact_by_id_get_it_with_id_should_return_None(self):
        ctod = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctod)
        self.contactDAO.delete_by_id(1)
        res = self.contactDAO.get_by_id(1)
        self.assertIsNone(res, "getting a deleted contact by id does not return None")

    def test_deleting_undefined_id_should_return_zero(self):
        res = self.contactDAO.delete_by_id(1)
        self.assertEqual(res, 0, "undefined id deletion does not return 0")

    def test_after_deleting_contact_by_names_get_item_with_id_should_return_None(self):
        ctod = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctod)
        self.contactDAO.delete_by_names("Bob", "Kump")
        res = self.contactDAO.get_by_id(1)
        self.assertIsNone(res, "getting by id a deleted contact by name does not return None")

    def test_deleting_not_existed_contact_should_return_zero(self):
        res = self.contactDAO.delete_by_names("Bob", "Kump")
        self.assertEqual(res, 0, "deleting non existant contact by name does not return 0")
        res = self.contactDAO.delete_by_id(1)
        self.assertEqual(res, 0, "deleting non existant contact by id does not return 0")

    def test_update_contact_should_set_the_provided_values(self):
        ctou = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        ctoc = Contact(1, "John", "Dough", "450-221-998", "john.dough@coldmail.com", False, 40.8)
        self.contactDAO.add(ctou)
        self.contactDAO.update(ctoc)
        res = self.contactDAO.get_by_names("John", "Dough")
        self.areContactAttribsEqual(ctoc, res)

    def test_update_contact_should_return_zero_if_id_does_not_exist(self):
        ctou = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        res = self.contactDAO.update(ctou)
        self.assertEqual(res, 0, "updating a non existant contact id does not return 0")

    def test_list_contacts_with_no_contacts_added_returns_empty_list(self):
        res = self.contactDAO.list()
        self.assertEqual(len(res), 0, "list does not return an empty list on empty database")
    
    def test_list_contacts_with_one_contact_should_return_list_with_contact(self):
        ctoa = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctoa)
        res = self.contactDAO.list()
        self.assertEqual(len(res), 1, "list does not return a list of count = 1 when only 1 contact is in database")
        self.areContactAttribsEqual(ctoa, res[0])
    
    def test_list_contacts_with_updated_False_and_all_items_updated_should_return_empty_list(self):
        ctoa = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctoa)
        res = self.contactDAO.list(False)
        self.assertEqual(len(res), 0, "list does not return an empty list when all contacts are updated and list was called with update = False")
    
    def test_list_contacts_with_updated_True_and_all_items_not_updated_should_return_empty_list(self):
        ctoa = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", False, 22.9)
        self.contactDAO.add(ctoa)
        res = self.contactDAO.list(True)
        self.assertEqual(len(res), 0, "list does not return an empty list when all contacts are not updated and list was called with updated = True")
    
    def test_list_contacts_with_all_not_updated_items_and_updated_False_should_return_all_contacts(self):
        ctoa = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", False, 22.9)
        self.contactDAO.add(ctoa)
        res = self.contactDAO.list(False)
        self.assertEqual(len(res), 1, "list does not return all updated contacts when list was called with updated = False")

    def test_list_contacts_with_all_updated_items_and_updated_True_should_return_all_contacts(self):
        ctoa = Contact(3, "Bob", "Kump", "514-554-223", "bob.kump@mailmail.com", True, 22.9)
        self.contactDAO.add(ctoa)
        res = self.contactDAO.list(True)
        self.assertEqual(len(res), 1, "list does not return all updated contacts when list was called with updated = True")

if __name__ == '__main__':
    unittest.main()
    
