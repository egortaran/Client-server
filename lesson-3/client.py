"""Программа-клиент"""

import sys
import json
import socket
import time

from common.variables import RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message

from client_func.connect_client import connect_client
from client_func.create_presence import create_presence
from client_func.sent_message import sent_message


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 201:
            return '201 : OK, create_presence'
        elif message[RESPONSE] == 202:
            return '202 : OK, connect_client'
        elif message[RESPONSE] == 203:
            return '203 : OK, sent_message'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    check_func = [
        create_presence(),
        connect_client(),
        sent_message(),
    ]

    for func in check_func:
        # Инициализация сокета и обмен

        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))

        time.sleep(0.5)
        message_to_server = func
        send_message(transport, message_to_server)
        try:
            answer = process_ans(get_message(transport))
            print(answer)
        except (ValueError, json.JSONDecodeError):
            print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
