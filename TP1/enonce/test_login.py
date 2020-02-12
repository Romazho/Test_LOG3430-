import unittest
import sys
from unittest.mock import patch
from models import Contact
from DAOs import ContactDAO
from login import login
from datetime import timedelta, datetime

# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.db_file = 'yourdb.db'
        self.contactDAO = ContactDAO(self.db_file)
        self.contactDAO.init_db()
    
    @patch('builtins.input', side_effect = ['Hakim', 'lol', 'n'])
    def test_when_login_is_called_and_results_are_none_and_user_outputs_is_n_it_should_sleep(self, mock):
        login()


if __name__ == '__main__':
    unittest.main()
