import unittest
import sqlite3
import builtins
from unittest.mock import patch
from models import Contact
import login as log
from unittest.mock import Mock

class TestLogin(unittest.TestCase):
    invalidUsername = "FFFFF"
    invalidPassword = "FFFFF"

    def setUp(self):
        self.db_file = 'yourdb.db'
        builtins.print = Mock()

        contact1 = Contact(12, "Hercules", "The God", "123456", "hercules.thegod@email.com", True, 2232)
        contact2 = Contact(15, "Sponge", "Bob", "99885", "sponge.bob@email.com", True, 55446)
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS
                                contact
                            (id INTEGER PRIMARY KEY,
                            first_name text,
                            last_name text,
                            phone text,
                            mail text,
                            updated bool,
                            updated_date double
                                )
                            ''')
            cursor.execute('''
                            INSERT INTO
                                contact
                            (first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date)
                            VALUES
                            (?,?,?,?,?,?)
                            ''', (
                contact2.first_name, contact2.last_name, contact2.phone, contact2.mail, contact2.updated,
                contact2.updated_date))
            connection.commit()
            cursor.execute('''
                            INSERT INTO
                                contact
                            (first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date)
                            VALUES
                            (?,?,?,?,?,?)
                            ''', (
                contact1.first_name, contact1.last_name, contact1.phone, contact1.mail, contact1.updated,
                contact1.updated_date))
            connection.commit()

    
    
    #On test le cas où l'utilisateur existe, son mot de passe est correct et il réussit à se déconnecter
    @patch('builtins.input', side_effect = ["hercules.thegod@email.com", "123456", invalidUsername , invalidPassword, 'n'])
    def test_when_login_is_called_and_username_and_password_are_correct(self, mock):
        log.login()
        self.assertEqual(builtins.print.call_count, 3)

    #On test le cas où l'utilisateur existe, mais il entre un mauvais mot de passe
    @patch('builtins.input', side_effect = ["hercules.thegod@email.com", invalidPassword, 'n'])
    def test_when_login_is_called_and_password_is_incorrect(self, mock):
        log.login()
        self.assertEqual(builtins.print.call_count, 2)

    #On test le cas où l'utilisateur rate son login une première fois, mais à la 2e fois il réussit, et ensuite il quitte en entrant un utilisateur qui n'existe pas et il entre 'n'
    @patch('builtins.input', side_effect = ["hercules.thegod@email.com", invalidPassword, 'o', "hercules.thegod@email.com", "123456", invalidUsername , invalidPassword, 'n'])
    def test_when_login_is_correct_on_second_try(self, mock):
        log.login()
        self.assertEqual(builtins.print.call_count, 4)

    #On test le cas où l'utilisateur n'existe pas dans la base de données
    @patch('builtins.input', side_effect = [invalidUsername, invalidPassword, 'n'])
    def test_when_login_is_called_and_results_are_none_and_user_inputs_n_it_should_sleep(self, mock):
        log.login()
        self.assertEqual(builtins.print.call_count, 2)


if __name__ == '__main__':
    unittest.main()
