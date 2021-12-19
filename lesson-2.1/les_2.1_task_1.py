from subprocess import Popen, PIPE

IP_ADDRESSES = ['google.com', 'yandex.ru', 'yahoo.com']


def ping_ip(ip_address):
    args = ['ping', '-n', '5', ip_address]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)

    code = reply.wait()
    if code == 0:
        return True
    else:
        return False


def host_ping(ip_addresses):
    for adr in ip_addresses:
        print('Узел доступен' if ping_ip(adr) else 'Узел недоступен')


host_ping(IP_ADDRESSES)
