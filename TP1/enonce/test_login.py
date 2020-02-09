import unittest
from unittest.mock import Mock
from models import Contact
from login import login
from datetime import timedelta, datetime


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.contactDAO = Mock()
        # self.contactService = ContactService(self.contactDAO)

    def test_when_login_is_called_and_results_are_none_and_user_outputs_n_it_should_sleep(self):
        login()
        # self.contactDAO.add.return_value = 1
        # self.assertRaises(AlreadyExistedItem, self.contactService.create_contact,
        #                   'Houssem', 'Ben Braiek', '123-456-7891', 'houssem.bb@gmail.com')


if __name__ == '__main__':
    unittest.main()
