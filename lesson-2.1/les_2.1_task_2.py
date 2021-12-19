from ipaddress import ip_address

IP1 = ip_address('192.168.1.0')
IP2 = '192.168.1.' + input('Введите диапозон адрессов от 0 до 255: ')

try:
    IP2 = ip_address(IP2)
    for i in range(int(IP2) - int(IP1) + 1):
        print(IP1 + i)
except ValueError:
    print('Вы ввели неправильный диапозон')
