import unittest
from unittest.mock import Mock
from models import Contact
from services import ContactService
from datetime import timedelta, datetime
from services import AlreadyExistedItem
from services import UndefinedID
from services import NotExistedItem


class TestContactService(unittest.TestCase):

    def setUp(self):
        self.contactDAO = Mock()
        self.contactService = ContactService(self.contactDAO)

    # On test la valeur de l'attribut updated
    def test_when_contact_is_created_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        self.assertTrue(self.contact.updated)

    # On test la valeur de l'attribut updated_date
    def test_when_contact_is_created_updated_date_should_be_now(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        self.assertEqual(int(self.contact.updated_date),
                         int(datetime.now().timestamp()))

    # On test le cas où l'exception AlreadyExistedItem est levée
    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        self.contactDAO.add.return_value = 1
        self.assertRaises(AlreadyExistedItem, self.contactService.create_contact,
                          'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')

    # On test le cas où valeur de l'attribut updated est mise à True avec update_contact 
    def test_when_contact_is_changed_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        self.contact = self.contactService.create_contact(
            'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')
        constact = self.contactService.update_contact(
            None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')
        self.assertTrue(constact.updated)

    # On test la valeur de l'attribut updated_date
    def test_when_contact_is_changed_updated_date_should_be_now(self):
        constact = self.contactService.update_contact(
            None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')
        self.assertEqual(int(constact.updated_date),
                         int(datetime.now().timestamp()))

    # On test le cas de l'exception UndefinedID
    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.update.return_value = 0
        self.assertRaises(UndefinedID, self.contactService.update_contact,
                          None, 'Houssem', 'Ben Braiek', '123-456-7891', 'lol@gmail.com')

    # On test le cas de où id n'est pas None
    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        self.contactService.retrieve_contact(23, 'Gary', 'Simpson')
        self.contactDAO.get_by_id.assert_called_once_with(id=23)

    # On test le cas de où id est None
    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        self.contactService.retrieve_contact(None, 'Gary', 'Simpson')
        self.contactDAO.get_by_names.assert_called_once_with(
            first_name='Gary', last_name='Simpson')

    # On test le cas de l'exception UndefinedID
    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        self.contactDAO.get_by_id.return_value = None
        self.assertRaises(
            UndefinedID, self.contactService.retrieve_contact, 23, 'Gary', 'Simpson')

    # On test le cas de l'exception NotExistedItem
    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        self.contactDAO.get_by_names.return_value = None
        self.assertRaises(
            NotExistedItem, self.contactService.retrieve_contact, None, 'Gary', 'Simpson')

    # On test le cas de où id n'est pas None
    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        self.contactService.delete_contact(77, 'Harry', 'Shooter')
        self.contactDAO.delete_by_id.assert_called_once_with(77)

    # On test le cas de où id est None
    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        self.contactService.delete_contact(None, 'Harry', 'Shooter')
        self.contactDAO.delete_by_names.assert_called_once_with(
            'Harry', 'Shooter')

    # On test le cas de l'exception UndefinedID
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

    # On test le cas où le delta.days est plus grand que 1095
    def test_when_verify_contacts_status_is_called_and_delta_days_is_bigger_than_1095_it_should_call_DAO_deactivate(self):
        contact = Contact(1, 'first_name', 'last_name', 'phone',
                          'mail', True, datetime.now().timestamp() - 990000000)
        self.contactDAO.list.return_value = [contact]
        self.contactService.verify_contacts_status()
        self.contactDAO.deactivate.assert_called()

    # On test le cas où le delta.days est plus petit que 1095
    def test_when_verify_contacts_status_is_called_and_contact_is_new_it_should_not_call_DAO_deactivate(self):
        contact = Contact(1, 'first_name', 'last_name', 'phone',
                          'mail', True, datetime.now().timestamp())
        self.contactDAO.list.return_value = [contact]
        self.contactService.verify_contacts_status()
        self.contactDAO.assert_not_called()

    # On test les cas où le mail est de bon format
    def test_when_check_mail_is_called_with_correct_mail_it_should_return_true(self):
        self.assertTrue(self.contactService.check_mail("dude123@gmail.com"))
        self.assertTrue(self.contactService.check_mail("123@321.org"))
        self.assertTrue(self.contactService.check_mail(
            "this.is.a.legit.email.so.dont.email.me.thanks@gmail.lol"))

    # On test les cas où le mail est de mauvais format
    def test_when_check_mail_is_called_with_incorrect_mail_it_should_return_false(self):
        self.assertFalse(self.contactService.check_mail("not an Email lol"))
        self.assertFalse(self.contactService.check_mail("close@butNotEmail"))
        self.assertFalse(self.contactService.check_mail(
            "Still@Not.AnEmail_BecauseTooLong"))
        self.assertFalse(self.contactService.check_mail("123@@321.com"))
        self.assertFalse(self.contactService.check_mail("@dont.com"))
        self.assertFalse(self.contactService.check_mail("mail.me@.com"))

    # On test les cas où le numéro de téléphone est de bon format
    def test_when_check_phone_is_called_with_correct_number_it_should_return_true(self):
        self.assertTrue(self.contactService.check_phone("123-321-7777"))
        self.assertTrue(self.contactService.check_phone("999-999-9999"))
        self.assertTrue(self.contactService.check_phone("000-000-0000"))

    # On test les cas où le numéro de téléphone est de mauvais format
    def test_when_check_phone_is_called_with_incorrect_number_it_should_return_false(self):
        self.assertFalse(self.contactService.check_phone(""))
        self.assertFalse(self.contactService.check_phone("12 leter str"))
        self.assertFalse(self.contactService.check_phone("123@321@7777"))
        self.assertFalse(self.contactService.check_phone("33g-123-0000"))
        self.assertFalse(self.contactService.check_phone("332-1g3-0000"))
        self.assertFalse(self.contactService.check_phone("332-123-0a00"))


if __name__ == '__main__':
    unittest.main()
