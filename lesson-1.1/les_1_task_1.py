words = ["разработка", "сокет", "декоратор"]

for word in words:
    print(f'{word}: {type(word)}')
# разработка: <class 'str'>
# сокет: <class 'str'>
# декоратор: <class 'str'>

words.append("\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430")  # разработка
words.append("\u0441\u043e\u043a\u0435\u0442")  # сокет
words.append("\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440")  # декоратор

for word in words[3:6]:
    print(f'(Unicode) {word}: {type(word)}')
# (Unicode) разработка: <class 'str'>
# (Unicode) сокет: <class 'str'>
# (Unicode) декоратор: <class 'str'>
