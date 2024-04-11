import logging

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    blue = "\x1b[34;20m"  # добавлен синий цвет
    reset = "\x1b[0m"
    format = "%(asctime)s %(name)s %(levelname)s %(message)s [%(filename)s:%(lineno)d]"

    FORMATS = {
        logging.DEBUG: blue + format + reset,  # DEBUG теперь синий
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# Создание объекта логгера
logger = logging.getLogger("PORN_LOGS")
logger.setLevel(logging.DEBUG)

# Создание обработчика для консольного вывода
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Установка кастомного форматтера
ch.setFormatter(CustomFormatter())

# Добавление обработчика к логгеру
logger.addHandler(ch)
