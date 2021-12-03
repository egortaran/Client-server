import logging.handlers

# Создаём объект-логгер с именем server_log.main
LOG = logging.getLogger('server_log.main')

# Создаём объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s ")

# Создать обработчик
FILE_HANDLER = logging.FileHandler("server.log", encoding='utf-8')

# подключить объект Formatter к обработчику
FILE_HANDLER.setFormatter(FORMATTER)

# Добавить обработчик к регистратору
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

TIMED_ROTATING = logging.handlers.TimedRotatingFileHandler('server.log', encoding='utf8', interval=1, when='D')


if __name__ == '__main__':
    # Передать сообщение обработчику
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
    LOG.warning('Предупреждение')
    LOG.error('Ошибка')
    LOG.critical('Критическое общение')
