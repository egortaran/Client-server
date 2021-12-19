from ipaddress import ip_address

from tabulate import tabulate


def host_range_ping_tab():  # Функция №3
    IP1 = ip_address('192.168.1.0')
    IP2 = '192.168.1.' + input('Введите диапозон адрессов от 0 до 255: ')

    my_dict = {'Reachable': [], 'Unreachable': []}

    try:
        IP2 = ip_address(IP2)
        for i in range(int(IP2) - int(IP1) + 1):
            my_dict['Reachable'].append(IP1 + i)
    except ValueError:
        my_dict['Unreachable'].append(IP2)
        print('Вы ввели неправильный диапозон')
    print(tabulate(my_dict, headers='keys'))

