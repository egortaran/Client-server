import time
from common.variables import ACTION, TIME, MESSAGE, FROM, TO, AUTHENTICATE, MSG, USER, ACCOUNT_NAME, PASSWORD, PRESENCE


def connect_client(account_name='Guest'):
    """
    Функция генерирует запрос входа клиента
    """
    out = {
        ACTION: AUTHENTICATE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name,
            PASSWORD: 'this_is_password'
        }
    }
    return out
