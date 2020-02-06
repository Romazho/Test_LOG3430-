import unittest
from unittest.mock import Mock
from models import Contact
from services import ContactService
from datetime import timedelta, datetime
from services import AlreadyExistedItem
from services import UndefinedID
from services import NotExistedItem

# To complete...


class TestContactService(unittest.TestCase):

    def setUp(self):
        self.contactDAO = Mock()
        self.contactService = ContactService(self.contactDAO)
        # Preparation for the next tests

    def test_when_contact_is_created_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        self.assertTrue(self.contact.updated)

    def test_when_contact_is_created_updated_date_should_be_now(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        self.assertEqual(int(self.contact.updated_date),
                         int(datetime.now().timestamp()))

    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        self.contactDAO.add.return_value = 1
        self.assertRaises(AlreadyExistedItem, self.contactService.create_contact,
                          'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')

    def test_when_contact_is_changed_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        constact = self.contactService.update_contact(
            None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')
        self.assertTrue(constact.updated)

    def test_when_contact_is_changed_updated_date_should_be_now(self):
        constact = self.contactService.update_contact(
            None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')
        self.assertEqual(int(constact.updated_date),
                         int(datetime.now().timestamp()))

    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.update.return_value = 0
        self.assertRaises(UndefinedID, self.contactService.update_contact,
                          None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')

    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        self.contactService.retrieve_contact(23, 'Gary', 'Simpson')
        self.contactDAO.get_by_id.assert_called_once_with(id=23)

    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        self.contactService.retrieve_contact(None, 'Gary', 'Simpson')
        self.contactDAO.get_by_names.assert_called_once_with(
            first_name='Gary', last_name='Simpson')

    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        self.contactDAO.get_by_id.return_value = None
        self.assertRaises(
            UndefinedID, self.contactService.retrieve_contact, 23, 'Gary', 'Simpson')

    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        self.contactDAO.get_by_names.return_value = None
        self.assertRaises(
            NotExistedItem, self.contactService.retrieve_contact, None, 'Gary', 'Simpson')

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        self.contactService.delete_contact(77, 'Harry', 'Shooter')
        self.contactDAO.delete_by_id.assert_called_once_with(77)

    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        self.contactService.delete_contact(None, 'Harry', 'Shooter')
        self.contactDAO.delete_by_names.assert_called_once_with(
            'Harry', 'Shooter')

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.delete_by_id.return_value = 0
        self.assertRaises(
            UndefinedID, self.contactService.delete_contact, 77, 'some', 'dude')

    # hypothèse: le nom de la fonction est erroné, car la fonction retrieve ne call pas "delete_by_names", alors on a changé le nom de la fonction pour
    # test_when_delete... à la place de test_when_retrieve...
    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_returns_zero_it_should_raise_NotExistedItem(self):
        self.contactDAO.delete_by_names.return_value = 0
        self.assertRaises(
            NotExistedItem, self.contactService.delete_contact, None, 'oki', 'doki')

    def test_when_verify_contacts_status_is_called_and_delta_days_is_bigger_than_1095_it_should_call_DAO_deactivate(self):
        contact = Contact(1, 'first_name', 'last_name', 'phone',
                          'mail', True, datetime.now().timestamp() - 990000000)
        self.contactDAO.list.return_value = [contact]
        self.contactService.verify_contacts_status()
        self.contactDAO.deactivate.assert_called()

    def test_when_verify_contacts_status_is_called_and_contact_is_new_it_should_not_call_DAO_deactivate(self):
        contact = Contact(1, 'first_name', 'last_name', 'phone',
                          'mail', True, datetime.now().timestamp())
        self.contactDAO.list.return_value = [contact]
        self.contactService.verify_contacts_status()
        self.contactDAO.assert_not_called()


if __name__ == '__main__':
    unittest.main()
