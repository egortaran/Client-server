"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого: Создать функцию write_order_to_json(), в которую
передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в
4 пробельных символа; Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений
каждого параметра.
"""

import json
import os
from datetime import datetime


def write_order_to_json(item="Phone", quantity='1', price='100', buyer='Alex', date=str(datetime.now().date())):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date,
    }

    sPATH = os.getcwd() + '/files/orders.json'
    with open(sPATH) as f_n:
        data = json.load(f_n)

    with open(sPATH, 'w') as f_n:
        link_data = data['orders']
        link_data.append(dict_to_json)
        json.dump(data, f_n, indent=4)


write_order_to_json(item="Phone", quantity='1', price='100', buyer='Alex', date=str(datetime.now().date()))
write_order_to_json(item="TV", quantity='2', price='500', buyer='Oleg', date=str(datetime.now().date()))
write_order_to_json(item="Laptop", quantity='3', price='1000', buyer='Egor', date=str(datetime.now().date()))
