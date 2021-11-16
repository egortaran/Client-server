words = [b"class", b"function", b"method"]

for word in words:
    print(f'{word}: {type(word)}, len {len(word)}')
# b'class': <class 'bytes'>, len 5
# b'function': <class 'bytes'>, len 8
# b'method': <class 'bytes'>, len 6