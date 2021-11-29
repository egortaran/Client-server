import time
from common.variables import ACTION, MSG, TIME, MESSAGE, FROM, TO


def sent_message(account_name_from='Guest_from', account_name_to='Guest_to', message='Hello'):
    """
    Функция генерирует запрос сообщение клиента
    """
    out = {
        ACTION: MSG,
        TIME: time.time(),
        TO: account_name_to,
        FROM: account_name_from,
        MESSAGE: message,
    }
    return out
