# Импорт настраиваемого логгера из файла logger.py
from logger import logger

def some_function():
    try:
        # Некоторая логика
        logger.debug("Это сообщение отладки")
        logger.info("Это информационное сообщение")
        logger.warning("Это предупреждение")
        logger.error("Это сообщение об ошибке")
        logger.critical("Это критическая ошибка")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}", exc_info=True)

if __name__ == "__main__":
    some_function()
