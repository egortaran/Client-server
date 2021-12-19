import subprocess

hosts = ["www.google.com", "www.yandex.ru", "www.youtube.com"]

for host in hosts:
    ping = subprocess.Popen(
        ["ping", "-c", "4", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    print(out.decode('CP866'))
