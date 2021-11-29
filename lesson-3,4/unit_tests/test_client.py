"""Unit-тесты клиента"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, MESSAGE, AUTHENTICATE, ERROR, TO, FROM, USER, MSG, PASSWORD, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import process_ans, create_presence, connect_client, sent_message


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_def_process_ans(self):
        """Тест функции process_ans"""
        self.assertEqual(process_ans({RESPONSE: 201}), '201 : OK, create_presence')
        self.assertEqual(process_ans({RESPONSE: 202}), '202 : OK, connect_client')
        self.assertEqual(process_ans({RESPONSE: 203}), '203 : OK, sent_message')
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

    def test_def_create_presence(self):
        """Тест функции create_presence"""
        test = create_presence(account_name='Guest')
        test[TIME] = 1.1

        answer = {
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        self.assertEqual(test, answer)

    def test_def_connect_client(self):
        """Тест функции connect_client"""
        test = connect_client(account_name='Guest')
        test[TIME] = 1.1

        answer = {
            ACTION: AUTHENTICATE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest',
                PASSWORD: 'this_is_password'
            }
        }
        self.assertEqual(test, answer)

    def test_def_sent_message(self):
        """Тест функции sent_message"""
        test = sent_message(account_name_from='Guest_from', account_name_to='Guest_to', message='Hello')
        test[TIME] = 1.1

        answer = {
            ACTION: MSG,
            TIME: 1.1,
            TO: 'Guest_to',
            FROM: 'Guest_from',
            MESSAGE: 'Hello',
        }
        self.assertEqual(test, answer)


if __name__ == '__main__':
    unittest.main()
