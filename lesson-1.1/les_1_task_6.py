my_list = ["сетевое программирование", "сокет", "декоратор"]

with open("test_file.txt", "w") as test_file:
    for my_str in my_list:
        test_file.write(my_str + '\n')

print(test_file.encoding)  # cp1251

with open("test_file.txt", "r", encoding="unicode-escape") as test_file:
    text = test_file.read()
    print(text)
# ñåòåâîå ïðîãðàììèðîâàíèå
# ñîêåò
# äåêîðàòîð
