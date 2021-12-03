import logging.handlers

# Создаём объект-логгер с именем client_log.main
LOG = logging.getLogger('client_log.main')

# Создаём объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s ")

# Создать обработчик
FILE_HANDLER = logging.FileHandler("client.log", encoding='utf-8')

# подключить объект Formatter к обработчику
FILE_HANDLER.setFormatter(FORMATTER)

# Добавить обработчик к регистратору
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Передать сообщение обработчику
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
    LOG.warning('Предупреждение')
    LOG.error('Ошибка')
    LOG.critical('Критическое общение')
