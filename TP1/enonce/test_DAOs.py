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
        self.contact1 = Contact(6, "R", "Z", "514999666", "Hakim@gmail.com", False, 20.3)
        self.contact2 = Contact(50, "H", "P", "514999666", "Hakim@gmail.com", False, 20.3)

    def compareWithContact1(self, newContact=None):
        if newContact is not None:
            assert self.contact1.first_name == newContact.first_name, "should be {}".format(self.contact1.first_name)
            assert self.contact1.last_name == newContact.last_name, "should be {}".format(self.contact1.last_name)
            assert self.contact1.phone == newContact.phone, "should be {}".format(self.contact1.phone)
            assert self.contact1.mail == newContact.mail, "should be {}".format(self.contact1.mail)
            assert self.contact1.updated == newContact.updated, "should be {}".format(self.contact1.updated)
            assert self.contact1.updated_date == newContact.updated_date, "should be {}".format(self.contact1.updated_date)


    def tearDown(self):
        os.remove(self.db_file)
    
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
        newContact = self.contactDAO.get_by_id(self.contactDAO.add(self.contact1))
        self.compareWithContact1(newContact)
    
    def test_get_by_names_after_add_should_return_inserted_value(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_names(self.contact1.first_name, self.contact1.last_name)
        self.compareWithContact1(newContact)

    def test_get_by_id_with_undefined_rowid_should_return_None(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_id(2)
        assert self.compareWithContact1(newContact) == None
    
    def test_get_by_names_with_notexisted_contact_should_return_None(self):
        self.contactDAO.add(self.contact1)
        newContact = self.contactDAO.get_by_names(self.contact2.first_name, self.contact2.last_name)
        assert self.compareWithContact1(newContact) == None
    
    def test_deactivate_contact_then_get_it_with_id_should_be_not_updated(self):
        pass
    
    def test_deactivate_contact_on_undefined_id_should_return_zero(self):
        pass
    
    def test_after_deleting_contact_by_id_get_it_with_id_should_return_None(self):
        pass

    def test_deleting_undefined_id_should_return_zero(self):
        pass

    def test_after_deleting_contact_by_names_get_item_with_id_should_return_None(self):
        pass

    def test_deleting_not_existed_contact_should_return_zero(self):
        pass

    def test_update_contact_should_set_the_provided_values(self):
        pass

    def test_update_contact_should_return_zero_if_id_does_not_exist(self):
        pass

    def test_list_contacts_with_no_contacts_added_returns_empty_list(self):
        pass
    
    def test_list_contacts_with_one_contact_should_return_list_with_contact(self):
        pass
    
    def test_list_contacts_with_updated_False_and_all_items_updated_should_return_empty_list(self):
        pass
    
    def test_list_contacts_with_updated_True_and_all_items_not_updated_should_return_empty_list(self):
        pass
    
    def test_list_contacts_with_all_not_updated_items_and_updated_False_should_return_all_contacts(self):
        pass

    def test_list_contacts_with_all_updated_items_and_updated_True_should_return_all_contacts(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
