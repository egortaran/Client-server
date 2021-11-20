"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого: Создать
функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В
этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий
список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия
столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для
этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла); Создать функцию
write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов
функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл; Проверить работу программы
через вызов функции write_to_csv().
"""

import csv
import os


def get_date():
    sPATH = os.getcwd() + '/files/'
    sFILES = ["info_1.txt", "info_2.txt", "info_3.txt"]

    os_prod_list, os_name_list, os_code_list, os_type_list = ([], [], [], [])

    main_data = [
        ["Изготовитель системы", os_prod_list],
        ["Название ОС", os_name_list],
        ["Код продукта", os_code_list],
        ["Тип системы", os_type_list]
    ]

    for file_name in sFILES:
        with open(sPATH + file_name, "r") as my_file:
            text = my_file.read()

            # Создание словаря из файла. Пример: {'Имя узла': 'Comp1', 'Версия ОС': '16299', ...}
            new_dict = {}
            slit_text = text.splitlines()
            for line in slit_text:
                split_line = line.split(':')
                new_dict[split_line[0]] = split_line[-1].strip()

            # Добавление списков
            for atr in main_data:
                atr[-1].append(new_dict[atr[0]])

    return main_data


def write_to_csv(csv_file):
    main_data = get_date()

    # Сохранение подготовленных данных в CSV формат
    new_list = [[]]
    for el in main_data:
        new_list[0].append(el[0])
        new_list.append(el[-1])

    # Запись данных в файл
    with open(csv_file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in new_list:
            f_n_writer.writerow(row)

    # Чтение CSV файла
    with open(csv_file) as f_n:
        print(f_n.read())


write_to_csv(csv_file='csv_file.csv')
