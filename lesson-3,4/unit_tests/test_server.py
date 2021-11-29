"""Unit-тесты сервера"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, TO, FROM, MESSAGE, MSG, PASSWORD, AUTHENTICATE, USER, ACCOUNT_NAME, TIME, \
    ACTION, PRESENCE
from server import process_client_message


class TestServer(unittest.TestCase):
    """
    В сервере только 1 функция для тестирования
    """
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    ok_dict_PRESENCE = {RESPONSE: 201}
    ok_dict_AUTHENTICATE = {RESPONSE: 202}
    ok_dict_MSG = {RESPONSE: 203}

    def test_def_process_client_message(self):
        """Проверка функции process_client_message"""

        # Запрос PRESENCE
        answer_PRESENCE = {
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest',
                PASSWORD: 'this_is_password'
            }
        }
        self.assertEqual(process_client_message(answer_PRESENCE), self.ok_dict_PRESENCE)

        # Запрос AUTHENTICATE
        answer_AUTHENTICATE = {
            ACTION: AUTHENTICATE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest',
                PASSWORD: 'this_is_password'
            }
        }
        self.assertEqual(process_client_message(answer_AUTHENTICATE), self.ok_dict_AUTHENTICATE)

        # Запрос MSG
        answer_MSG = {
            ACTION: MSG,
            TIME: 1.1,
            TO: 'Guest_to',
            FROM: 'Guest_from',
            MESSAGE: 'Hello',
        }
        self.assertEqual(process_client_message(answer_MSG), self.ok_dict_MSG)

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()
