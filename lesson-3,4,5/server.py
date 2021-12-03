"""Программа-сервер"""
import logging
import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PASSWORD, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, AUTHENTICATE, MSG, TO, FROM
from common.utils import get_message, send_message

SERVER_LOGGER = logging.getLogger('server_log.main')
print(SERVER_LOGGER)

def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 201}
    elif ACTION in message and message[ACTION] == AUTHENTICATE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest' \
            and message[USER][PASSWORD] == 'this_is_password':
        return {RESPONSE: 202}
    elif ACTION in message and message[ACTION] == MSG and TIME in message \
            and TO in message and message[TO] == 'Guest_to' \
            and FROM in message and message[FROM] == 'Guest_from':
        return {RESPONSE: 203}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    :return:
    '''

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = 1
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        SERVER_LOGGER.critical('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.critical(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        SERVER_LOGGER.critical(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            print(message_from_cient)
            response = process_client_message(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            SERVER_LOGGER.error('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
